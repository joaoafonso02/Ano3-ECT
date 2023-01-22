/*
 *  \author ALL
 */

#ifndef __SOMM22__MODULE__PEQ__GROUP__
#define __SOMM22__MODULE__PEQ__GROUP__

#include "somm22.h"

#include <list>
#include <stdio.h>

namespace somm22
{

    namespace group 
    {

        namespace peq
        {
            /* ACTION POINT: Declare here your module's data structure as external */
            extern std::list<Event> PEQTable; // Process Event Queue row

        } // end of namespace peq

    } // end of namespace group

} // end of namespace somm22

#endif /* __SOMM22__MODULE__PEQ__GROUP__ */

