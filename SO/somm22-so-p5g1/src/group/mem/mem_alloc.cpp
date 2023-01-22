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

        void *memAlloc(uint32_t pid, uint32_t size)
        {
            soProbe(403, "%s(%u, 0x%x)\n", __func__, pid, size);

            require(pid > 0, "process ID must be non-zero");

            switch( mem::allocPolicy ) {
                case FirstFit:
                    return memFirstFitAlloc(pid, size);
                case NextFit:
                    return memNextFitAlloc(pid, size);
                case BestFit:
                    return memBestFitAlloc(pid, size);
                case WorstFit:
                    return memWorstFitAlloc(pid, size);
            }
            return NULL;
        }

// ================================================================================== //

    } // end of namespace group

} // end of namespace somm22

