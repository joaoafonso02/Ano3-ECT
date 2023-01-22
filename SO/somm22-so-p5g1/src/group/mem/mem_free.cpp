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

        void memFree(void *addr)
        {
            soProbe(408, "%s(addr: %p)\n", __func__, addr);

            require(addr != NULL, "addr must be non-null");

            // find block to be freed
            auto process = mem::MEMBusy.begin();
            for(auto it = mem::MEMBusy.begin(); it != mem::MEMBusy.end(); ++it){
                if( it->start == (void*) (uint64_t) addr ) {
                    process = it;
                    mem::MEMBusy.erase(it);
                    break;
                }
            }

            for(auto it = mem::MEMFree.begin(); it != mem::MEMFree.end(); ++it){
                if( (uint8_t*) it->start + it->size == process->start ) { // free space before
                    printf("Free space is before\n");
                    it->size += process->size;
                    uint32_t *itBackSize = &(it->size); // stores block that precedes process
                    ++it; // get next memory block
                    if( it->start == (uint8_t*) process->start + process->size ) { // free space before and after
                        *itBackSize += it->size; // join free blocks size and store it on 1st
                        mem::MEMFree.erase(it); // removes the 2nd block
                    }
                    return;
                } else if( it->start == (uint8_t*) process->start + process->size ) { // free space after
                    it->start = process->start;
                    it->size += process->size;
                    return;
                }
            }

            // instantiate block of exactly the same size and position of process
            mem::MMB newFreeBlock;
            newFreeBlock.PID = 0;
            newFreeBlock.size = process->size;
            newFreeBlock.start = process->start;

            // if there is no free memory neighbors just add the new memory block in order
            for(auto it = mem::MEMFree.begin(); it != mem::MEMFree.end(); ++it){
                if( it->start > process->start ) {
                    mem::MEMFree.insert(it, newFreeBlock);
                    return;
                }
            }

            // if there is no free memory block at all
            mem::MEMFree.push_back(newFreeBlock);
        }

// ================================================================================== //

    } // end of namespace group

} // end of namespace somm22
