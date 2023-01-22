/*
 *  \author ALL
 */

#ifndef __SOMM22__MODULE__PCT__GROUP__
#define __SOMM22__MODULE__PCT__GROUP__

#include "somm22.h"

#include <list>
#include <stdio.h>

#include <map>

namespace somm22
{
    
    namespace group 
    {

        namespace pct
        {
            /* ACTION POINT: Declare here your module's data structure as external */
            struct PCB {
                uint32_t PID;
                uint32_t arrivalTime;
                uint32_t duration;
                uint32_t addrSpaceSize;
                ProcessState state;
                int32_t startTime;
                void *memAddr; 
            };
            extern std::map<uint32_t, PCB> PCTable;

        } // end of namespace pct

    } // end of namespace group

} // end of namespace somm22

#endif /* __SOMM22__MODULE__PCT__GROUP__ */

