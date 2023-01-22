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

        void memInit(uint32_t mSize, uint32_t osSize, uint32_t cSize, AllocationPolicy allocPolicy) 
        {
            soProbe(401, "%s(0x%x, 0x%x, 0x%x, %s)\n", __func__, mSize, osSize, cSize, memAllocationPolicyAsString(allocPolicy));

            require(mSize > osSize, "memory must be bigger than the one use by OS");
            require((mSize % cSize) == 0, "memory size must be a multiple of chunck size");
            require((osSize % cSize) == 0, "memory size for OS must be a multiple of chunck size");

            mem::allocPolicy = allocPolicy;
            mem::maxAllowableSize = mSize - osSize;

            // creates os memory
            mem::MMB mmb;
            mmb.PID = 0;
            mmb.start = (void*) (uint64_t) osSize;
            mmb.size = mSize - osSize;

            mem::MEMFree.push_back(mmb);

            // throw Exception(ENOSYS, __func__);
        }

// ================================================================================== //

    } // end of namespace group

} // end of namespace somm22
