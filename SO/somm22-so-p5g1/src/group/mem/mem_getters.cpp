/*
 *  \author Eduardo Fernandes, João Ferreira, Pedro Durval
 */

#include "somm22.h"
#include "mem_module.h"

namespace somm22
{

    namespace group 
    {

// ================================================================================== //

        uint32_t memGetBiggestHole()
        {
            soProbe(409, "%s()\n", __func__);

            uint32_t biggest = 0;
            for (auto it = mem::MEMFree.begin(); it != mem::MEMFree.end(); ++it) {
                if (it->size > biggest) biggest = it->size;
            }
            return biggest;
        }

// ================================================================================== //

        uint32_t memGetMaxAllowableSize()
        {
            soProbe(409, "%s()\n", __func__);
            
            return mem::maxAllowableSize;
        }

// ================================================================================== //

    } // end of namespace group

} // end of namespace somm22