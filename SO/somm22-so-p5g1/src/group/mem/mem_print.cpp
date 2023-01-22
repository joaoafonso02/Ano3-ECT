/*
 *  \author ...
 */

#include "somm22.h"
#include "mem_module.h"

namespace somm22
{

    namespace group 
    {

        static void memWrite(FILE *f) {
            fprintf(f, "+==============================+\n");
            fprintf(f, "|  Memory Management busy list |\n");    
            fprintf(f, "+-------+-----------+----------+\n");
            fprintf(f, "|  PID  |   start   |   size   |\n");
            fprintf(f, "+-------+-----------+----------+\n");
            
            // iterate over pct table in order
            for(auto it = mem::MEMBusy.begin(); it!=mem::MEMBusy.end(); ++it) {
                // PID
                fprintf(f, "|  %3d  |", it->PID);

                // start location
                fprintf(f, " %9p |", it->start);

                // size
                fprintf(f, " %#8x |", it->size);

                fprintf(f, "\n");
            }
            fprintf(f, "+==============================+\n\n");


            fprintf(f, "+==============================+\n");
            fprintf(f, "|  Memory Management Free List |\n");
            fprintf(f, "+-------+-----------+----------+\n");
            fprintf(f, "|  PID  |   start   |   size   |\n");
            fprintf(f, "+-------+-----------+----------+\n");

            for(auto it = mem::MEMFree.begin(); it!=mem::MEMFree.end(); ++it){
                // PID
                fprintf(f, "|  ---  |");

                // start location
                fprintf(f, " %9p |", it->start);

                // size
                fprintf(f, " %#8x |", it->size);

                fprintf(f, "\n");
            }
            fprintf(f, "+==============================+\n\n");
        }

// ================================================================================== //

        void memLog()
        {
            soProbe(402, "%s()\n", __func__);

            memWrite(logGetStream());
        }

// ================================================================================== //

        void memPrint(const char *fname, PrintMode mode)
        {
            soProbe(402, "%s(\"%s\", %s)\n", __func__, fname, (mode == NEW) ? "NEW" : "APPEND");

            FILE* f;
            if( mode==NEW ) {
                f = fopen(fname, "w");
                memWrite(f);
            } else {
                f = fopen(fname, "a");
                memWrite(f);
            }

            fclose(f);
        }

// ================================================================================== //

    } // end of namespace group

} // end of namespace somm22
