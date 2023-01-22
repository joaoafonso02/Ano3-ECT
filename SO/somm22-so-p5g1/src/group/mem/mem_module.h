/*
 *  \author ALL
 */

#ifndef __SOMM22__MODULE__MEM__GROUP__
#define __SOMM22__MODULE__MEM__GROUP__

#include "somm22.h"
#include <list>

namespace somm22
{
    
    namespace group 
    {
        namespace mem
        {
            /* ACTION POINT: Declare here your module's data structure as external */
            struct MMB {
                uint32_t PID;
                void* start;
                uint32_t size;
            };
            extern std::list<MMB> MEMBusy; // MEM busy list
            extern std::list<MMB> MEMFree; // MEM free list
            extern AllocationPolicy allocPolicy;
            extern uint32_t maxAllowableSize;

        } // end of namespace mem

    } // end of namespace group

} // end of namespace somm22

#endif /* __SOMM22__MODULE__MEM__GROUP__ */

