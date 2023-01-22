/*
 *  \ Inês Moreira e Diogo Correia
 */

#include "somm22.h"
#include "peq_module.h"

#include <cstring>

namespace somm22
{

    namespace group 
    {


// ================================================================================== //

        const char *peqEventTypeAsString(EventType type)
        {
            soProbe(397, "%s(\"0x%x\")\n", __func__, type);

             switch( type ) {
                case ARRIVAL:
                    return "ARRIVAL";
                case POSTPONED:
                    return "POSTPONED";
                case TERMINATE:
                    return "TERMINATE";
                default:
                    return "";
            };
        }

// ================================================================================== //

         const char *peqEventMaskAsString(uint32_t mask)
        {
            soProbe(397, "%s(\"0x%x\")\n", __func__, mask);

            require((mask | 0b111) == 0b111, "wrong event mask");

            /* ACTION POINT: Replace next instruction with your code */
            
            char *maskStr = new char[25];
            
            // init maskStr
            strcpy(maskStr, "");

            // iterate through mask bits
            for (int i = 0; i < 3; i++)
            {
                // if bit is set, add event type to maskStr
                if (mask & (1 << i))
                {
                    strcat(maskStr, group::peqEventTypeAsString((EventType) (1 << i)));
                    strcat(maskStr, " | ");
                }
            }

            // remove trailing " | "
            if (strlen(maskStr) > 3)
                maskStr[strlen(maskStr) - 3] = '\0';
            
            return maskStr;
            // throw Exception(ENOSYS, __func__);
        }


// ================================================================================== //

    } // end of namespace group

} // end of namespace somm22

