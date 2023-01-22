/*
 *  \author ...
 */

#include "somm22.h"
#include "mem_module.h"

namespace somm22
{

    namespace group 
    {

// ================================================================================== //
        void *memNextFitAlloc(uint32_t pid, uint32_t size)
        {
            soProbe(405, "%s(%u, 0x%x)\n", __func__, pid, size);

            require(pid > 0, "process ID must be non-zero");

            static std::list<mem::MMB>::iterator lastMEM = mem::MEMFree.begin();

            // selects big enough space of free memory
            std::list<mem::MMB>::iterator free;
            bool found = false;
            std::list<mem::MMB>::iterator it = lastMEM;
            do {
                if( it->size >= size ) {
                    free = it;
                    found = true;
                    lastMEM = it;
                    break;
                }
                ++it;
            } while( it != lastMEM );

            if( !found ) return NULL;

            // add process to busy list
            mem::MMB process;
            process.PID = pid;
            process.size = size;
            process.start = free->start;

            // insert in order
            bool inserted = false;
            for(auto it = mem::MEMBusy.begin(); it != mem::MEMBusy.end(); ++it) {
                if( it->start > process.start ) {
                    mem::MEMBusy.insert(it, process);
                    inserted = true;
                    break;
                }
            }
            if( !inserted ) mem::MEMBusy.push_back(process);


            if( free->size == process.size ) { // if free block is the same size as the program then just remove it from the list
                mem::MEMFree.erase(free);
            } else { // just shorten the block to the new available size
                free->size -= process.size;
                free->start = (void*) ( (uint8_t*) free->start + process.size);
            }

            return process.start;
        }

// ================================================================================== //

    } // end of namespace group

} // end of namespace somm22