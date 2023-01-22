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

        uint32_t peqGetFirstPostponedProcess() 
        {
            soProbe(306, "%s()\n", __func__);

            /* ACTION POINT: Replace next instruction with your code */

            try {
                Event firstPostponed = peqPeekNext(EventType::POSTPONED);
                return firstPostponed.pid;
            } catch (Exception &e) {
                if( e.en == EINVAL ) return 0;
                else throw e;
            }
            
            // throw Exception(ENOSYS, __func__);
        }

// ================================================================================== //

    } // end of namespace group

} // end of namespace somm22

