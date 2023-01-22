/*
 *  \author Diogo Correia
 */

#include "somm22.h"
#include "peq_module.h"

namespace somm22
{

    namespace group 
    {

// ================================================================================== //

        void peqInsert(EventType type, uint32_t time, uint32_t pid)
        {
            soProbe(304, "%s(%s, %u, %u)\n", __func__, peqEventTypeAsString(type), time, pid);

            require(pid > 0, "process ID must be non-zero");

            /* ACTION POINT: Replace next instruction with your code */

            Event event;
            event.eventType = type;
            event.eventTime = time;
            event.pid = pid;

            peq::PEQTable.push_back(event);

            // order table by eventTime
            peq::PEQTable.sort([](Event a, Event b) { return a.eventTime < b.eventTime; });
            // throw Exception(ENOSYS, __func__);
        }

// ================================================================================== //

    } // end of namespace group

} // end of namespace somm22
