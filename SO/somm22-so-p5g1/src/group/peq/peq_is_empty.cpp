/*
 *  \author Diogo Correia
 */

#include "somm22.h"
#include "peq_module.h"

#include <algorithm>

namespace somm22
{

    namespace group 
    {

// ================================================================================== //

        bool peqIsEmpty(uint32_t mask) 
        {
            const char *maskStr = (mask == 0) ? "ANY" : ((mask == POSTPONED) ? "POSTPONED" : "ARRIVAL | TERMINATE");
            soProbe(303, "%s(%s)\n", __func__, maskStr);

            /* ACTION POINT: Replace next instruction with your code */
            
            std::list<Event> filteredEvents; 

            // filter PEQTable by the given mask if mask is not 0 (ANY)
            if( mask != 0 )
                std::copy_if(peq::PEQTable.begin(), peq::PEQTable.end(), std::back_inserter(filteredEvents), [mask](Event e) { return (e.eventType & mask) != 0; });
            else
                filteredEvents = peq::PEQTable;

            return filteredEvents.empty();
            // throw Exception(ENOSYS, __func__);
        }

// ================================================================================== //

    } // end of namespace group

} // end of namespace somm22

