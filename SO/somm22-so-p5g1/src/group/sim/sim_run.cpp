/*
 *  \author ...
 */

#include "somm22.h"
#include "sim_module.h"

namespace somm22
{

    namespace group
    {

        // ================================================================================== //

        /*
         * Solution may be based on a state machine with two states, which are related to the
         * type of events that are fetched from the Process Event Queue.
         * The meaningful cases are:
         * - ARRIVAL | TERMINATE
         * - POSTPONED
         */
        void simRun(uint32_t cnt)
        {
            soProbe(503, "%s(cnt: %u)\n", __func__, cnt);

            for (uint32_t i = 0; i < cnt; i++)
            {
                // get event from Process Event Queue
                Event event = peqFetchNext(sim::event_mask);

                sim::steps++;
                sim::event_mask = 0b101;

                if (event.eventType == EventType::ARRIVAL)
                {
                    sim::time = event.eventTime;
                    uint32_t processSize = pctGetProcessAddressSpaceSize(event.pid);

                    // discard process if its size > max mem
                    if (processSize > memGetMaxAllowableSize())
                    {
                        pctSetProcessState(event.pid, ProcessState::DISCARDED);
                    }
                    else if (processSize >= memGetBiggestHole() || peqGetFirstPostponedProcess() != 0)
                    { // postpone process if its size > available mem
                        pctSetProcessState(event.pid, ProcessState::SWAPPED);
                        peqInsert(EventType::POSTPONED, event.eventTime, event.pid);
                    }
                    else
                    {
                        // alloc memory to the process
                        void *memaddr = memAlloc(event.pid, processSize);

                        // PCT setters
                        pctSetProcessState(event.pid, ProcessState::RUNNING);
                        pctSetProcessStartTime(event.pid, event.eventTime);
                        pctSetProcessMemAddress(event.pid, memaddr);

                        // update PEQ
                        peqInsert(EventType::TERMINATE, event.eventTime + pctGetProcessDuration(event.pid), event.pid);
                    }
                }
                else if (event.eventType == EventType::POSTPONED)
                {
                    uint32_t processSize = pctGetProcessAddressSpaceSize(event.pid);

                    void *memaddr = memAlloc(event.pid, processSize);

                    // PCT setters
                    pctSetProcessState(event.pid, ProcessState::RUNNING);
                    pctSetProcessStartTime(event.pid, event.eventTime);
                    pctSetProcessMemAddress(event.pid, memaddr);

                    // update PEQ
                    peqInsert(EventType::TERMINATE, sim::time + pctGetProcessDuration(event.pid), event.pid);
                }
                else if (event.eventType == EventType::TERMINATE)
                {
                    sim::time = event.eventTime;
                    pctSetProcessState(event.pid, ProcessState::FINISHED);
                    memFree(pctGetProcessMemAddress(event.pid));
                }

                uint32_t postponedPID = peqGetFirstPostponedProcess();
                if (postponedPID)
                {
                    uint32_t processSize = pctGetProcessAddressSpaceSize(postponedPID);
                    if (processSize <= memGetBiggestHole())
                    {
                        sim::event_mask = 0b010;
                    }
                }

                // // finish process if running and time + duration = now
                // if (pctGetStateName(event.pid) == pctStateAsString(ProcessState::RUNNING) && event.eventTime == pctGetProcessDuration(event.pid))
                // {
                //     pctSetProcessState(event.pid, ProcessState::FINISHED);
                //     memFree(pctGetProcessMemAddress(event.pid));
                //     continue;
                // }
            }
        }

        // ================================================================================== //

    } // end of namespace group

} // end of namespace somm22
