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
        bool eventCompare(Event a, Event b) { return a.eventTime == b.eventTime && a.eventType == b.eventType && a.pid == b.pid; };

        Event peqFetchNext(uint32_t mask)
        {
            const char *maskStr = (mask == 0) ? "ANY" : ((mask == POSTPONED) ? "POSTPONED" : "ARRIVAL | TERMINATE");
            soProbe(305, "%s(%s)\n", __func__, maskStr);

            /* ACTION POINT: Replace next instruction with your code */

            Event nextEvent = peqPeekNext(mask);

            // remove the event from the PEQTable
            peq::PEQTable.remove_if([nextEvent](Event e) { return eventCompare(nextEvent, e); });

            return nextEvent;
            // throw Exception(ENOSYS, __func__);
        }

// ================================================================================== //

        Event peqPeekNext(uint32_t mask)
        {
            const char *maskStr = (mask == 0) ? "ANY" : ((mask == POSTPONED) ? "POSTPONED" : "ARRIVAL | TERMINATE");
            soProbe(305, "%s(%s)\n", __func__, maskStr);

            /* ACTION POINT: Replace next instruction with your code */

            std::list<Event> filteredEvents;            

            // filter PEQTable by the given mask
            std::copy_if(peq::PEQTable.begin(), peq::PEQTable.end(), std::back_inserter(filteredEvents), [mask](Event e) { return (e.eventType & mask) != 0; });
            
            // throw EINVAL Exception if no event is found (if filteredEvents is empty)
            if( filteredEvents.empty() ) {
                throw Exception(EINVAL, __func__);
            }

            // get the latest inserted
            filteredEvents.sort([](Event a, Event b) { return a.eventTime < b.eventTime; });

            return filteredEvents.front();
            // throw Exception(ENOSYS, __func__);
        }

// ================================================================================== //

    } // end of namespace group

} // end of namespace somm22
