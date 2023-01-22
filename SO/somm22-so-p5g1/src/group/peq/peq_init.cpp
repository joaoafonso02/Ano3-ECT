/*
 *  \author Diogo Correia
 */

#include "somm22.h"
#include "peq_module.h"

#include <fstream>
#include <iostream>

namespace somm22
{

    namespace group 
    {

// ================================================================================== //

        void peqInit(const char *fname)
        {
            soProbe(301, "%s(\"%s\")\n", __func__, fname);

            /* ACTION POINT: Replace next instruction with your code */
            std::ifstream MyReadFile(fname);
            std::string line;
            while( getline(MyReadFile, line) ) {
                if( line.at(0)=='#' ) continue;

                int size = 2;
                uint32_t v[size];
                for(int i=0; i<size; i++ ) {
                    int f = line.find(';');
                    int base = i!=3 ? 10 : 16;
                    v[i] = std::stoi(line.substr(0,f), nullptr, base);
                    line = line.substr(f+1);
                }

                peqInsert(EventType::ARRIVAL, v[1], v[0]);
            }
            MyReadFile.close();

            // throw Exception(ENOSYS, __func__);
        }

// ================================================================================== //

    } // end of namespace group

} // end of namespace somm22

