/*
 *  \author ALL
 */

#include "somm22.h"
#include "mem_module.h"

namespace somm22
{
    namespace group 
    {
        namespace mem
        {
            /* ACTION POINT: Declare here your module's internal data structure */
            std::list<MMB> MEMBusy;
            std::list<MMB> MEMFree;

            AllocationPolicy allocPolicy;

            uint32_t maxAllowableSize;
        } // end of namespace mem

    } // end of namespace group

} // end of namespace somm22
