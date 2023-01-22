/*
 *  \author João Ferreira
 */

#include "somm22.h"
#include "sim_module.h"

namespace somm22 
{

    namespace group
    {

// ================================================================================== //

        /*
         * \brief Init the module's internal data structure
         */
        void simInit()
        {
            soProbe(501, "%s()\n", __func__);

            /* ACTION POINT: Replace next instruction with your code */
            // throw Exception(ENOSYS, __func__);

            sim::steps = 0;
            sim::time = 0;
            sim::event_mask = 0b101;

        }

// ================================================================================== //

    } // end of namespace group

} // end of namespace somm22
