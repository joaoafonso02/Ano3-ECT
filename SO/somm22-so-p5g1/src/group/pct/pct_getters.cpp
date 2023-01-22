/*
 *  \author Diogo Correia, Inês Moreira
 */

#include "somm22.h"
#include "pct_module.h"

namespace somm22
{

    namespace group 
    {

// ================================================================================== //

        uint32_t pctGetProcessDuration(uint32_t pid)
        {
            soProbe(204, "%s(%d)\n", __func__, pid);

            require(pid > 0, "process ID must be non-zero");

            /* ACTION POINT: Replace next instruction with your code */
            return pct::PCTable[pid].duration;
        }
       

// ================================================================================== //

        uint32_t pctGetProcessAddressSpaceSize(uint32_t pid)
        {
            soProbe(205, "%s(%d)\n", __func__, pid);

            require(pid > 0, "process ID must be non-zero");

            /* ACTION POINT: Replace next instruction with your code */
            return pct::PCTable[pid].addrSpaceSize;
        }

// ================================================================================== //

        void *pctGetProcessMemAddress(uint32_t pid)
        {
            soProbe(206, "%s(%d)\n", __func__, pid);

            require(pid > 0, "process ID must be non-zero");

            /* ACTION POINT: Replace next instruction with your code */
            return pct::PCTable[pid].memAddr;
        }

// ================================================================================== //

        const char *pctGetStateName(uint32_t pid)
        {
            soProbe(210, "%s(\"%u\")\n", __func__, pid);

            /* ACTION POINT: Replace next instruction with your code */
            return pctStateAsString(pct::PCTable[pid].state); 
        }
        


// ================================================================================== //

    } // end of namespace group

} // end of namespace somm22
