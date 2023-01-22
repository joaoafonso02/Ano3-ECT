/*
 *  \author Pedro Durval & Eduardo
 */

#include "somm22.h"
#include "pct_module.h"

#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>

namespace somm22
{

    namespace group 
    {

// ================================================================================== //
        static void pctWrite(FILE *f) {
            fprintf(f, "+====================================================================================+\n");
            fprintf(f, "|                               Process Control Table                                |\n");
            fprintf(f, "+-------+-------------+----------+---------------+-----------+-----------------------+\n");
            fprintf(f, "|  PID  | arrivalTime | duration | addrSpaceSize |   state   | startTime |  memAddr  |\n");
            fprintf(f, "+-------+-------------+----------+---------------+-----------+-----------------------+\n");
            
            // iterate over pct table in order
            for(auto it = pct::PCTable.begin(); it!=pct::PCTable.end(); ++it) {
                // PID
                fprintf(f, "| %5d |", it->second.PID);

                // arrivalTime
                fprintf(f, " %11d |", it->second.arrivalTime);

                // duration
                fprintf(f, " %8d |", it->second.duration);

                // addrSpaceSize
                fprintf(f, " %#13x |", it->second.addrSpaceSize);

                // state
                fprintf(f, " %9s |", pctStateAsString(it->second.state));
                
                // startTime
                if( it->second.startTime!=-1 ) {
                    fprintf(f, " %9d |", it->second.startTime);
                } else {
                    fprintf(f, "   (nil)   |");
                }

                // memAddr
                if( it->second.memAddr!=nullptr ) {
                    fprintf(f, " %9p |", it->second.memAddr);
                } else {
                    fprintf(f, "   (nil)   |");
                }

                fprintf(f, "\n");
            }

            fprintf(f, "+====================================================================================+\n\n");
        }

        void pctPrint(const char *fname, PrintMode mode)
        {
            soProbe(202, "%s(\"%s\", %s)\n", __func__, fname, (mode == NEW) ? "NEW" : "APPEND");

            /* ACTION POINT: Replace next instruction with your code */
            FILE* f;
            if( mode==NEW ) {
                f = fopen(fname, "w");
            } else {
                f = fopen(fname, "a");
            }

            pctWrite(f);

            fclose(f);

            // throw Exception(ENOSYS, __func__);
        }

// ================================================================================== //

        void pctLog()
        {
            soProbe(202, "%s()\n", __func__);

            /* ACTION POINT: Replace next instruction with your code */
            pctWrite(logGetStream());
        }


// ================================================================================== //

    } // end of namespace group

} // end of namespace somm22
