/*
 *  \author ALL
 */

#include "somm22.h"
#include "pct_module.h"

namespace somm22
{

    namespace group 
    {

// ================================================================================== //

        void pctInsert(uint32_t pid, uint32_t arrivalTime, uint32_t duration, uint32_t addrSpaceSize)
        {
            soProbe(203, "%s(%d, %u, %u, 0x%x)\n", __func__, pid, arrivalTime, duration, addrSpaceSize);

            /* ACTION POINT: Replace next instruction with your code */
            pct::PCB row;
            row.PID = pid;
            row.arrivalTime = arrivalTime;
            row.duration = duration;
            row.addrSpaceSize = addrSpaceSize;
            row.state = ProcessState::TO_COME;
            row.startTime = -1;
            row.memAddr = NULL;
            pct::PCTable[pid] = row;
            // throw Exception(ENOSYS, __func__);
        }

// ================================================================================== //

    } // end of namespace group

} // end of namespace somm22
