   /*
 *  \Inês Moreira e Diogo Correia
 */

#include "somm22.h"
#include "peq_module.h"

namespace somm22
{

    namespace group 
    {
 
// ================================================================================== //
        static void peqWrite(FILE *f){

            fprintf(f, "+==============================+\n");
            fprintf(f, "|     Process Event Queue      |\n");
            fprintf(f, "+------------+-----------+-----+\n");
            fprintf(f, "|  eventTime | eventType | PID |\n");
            fprintf(f, "+------------+-----------+-----+\n");
            
            for(auto it = peq::PEQTable.begin(); it!=peq::PEQTable.end(); ++it)
            { 
                // begin row
                fprintf(f, "|");

                // eventTime
                fprintf(f, "%11d |", it-> eventTime);

                // eventType
                fprintf(f, "%10s |", peqEventTypeAsString(it-> eventType));

                // pid
                fprintf(f, "%4d |", it-> pid);
            
                // end row
                fprintf(f, "\n");
            }
            // end table
            fprintf(f, "+==============================+\n\n");
        }

        void peqLog()
        {   
            soProbe(302, "%s()\n", __func__);

            /* ACTION POINT: Replace next instruction with your code */
           
            peqWrite(logGetStream());
        }

// ================================================================================== //

        void peqLogEvent(Event *e, const char *msg)
        {
            soProbe(302, "%s(...)\n", __func__);

            fprintf(logGetStream(), "%s: (%s, %d, %d)\n", msg, peqEventTypeAsString(e->eventType), e->eventTime, e->pid);
        }

// ================================================================================== //

      
        void peqPrint(const char *fname, PrintMode mode)
        {
            soProbe(302, "%s(\"%s\", %s)\n", __func__, fname, (mode == NEW) ? "NEW" : "APPEND");

             FILE* f;
            if (mode == NEW) {
                f = fopen(fname, "w");
            } else {
                f = fopen(fname, "a");
            }

            if (f == NULL) {
                throw Exception(errno, __func__);
            }

            peqWrite(f);

            fclose(f);
        }

// ================================================================================== //

    } // end of namespace group

} // end of namespace somm22

