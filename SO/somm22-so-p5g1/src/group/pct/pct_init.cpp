/*
 *  \author João Ferreira, Eduardo Fernandes
 */

#include "somm22.h"
#include "pct_module.h"

#include <string>
#include <fstream>
#include <iostream>

namespace somm22
{

    namespace group 
    {

// ================================================================================== //

        void pctInit(const char *fname) 
        {
            soProbe(201, "%s(\"%s\")\n", __func__, fname);

            /* ACTION POINT: Replace next instruction with your code */

            // Uncomment to use manual inserts
            // pctInsert(222,0,100,0x400);
            // pctInsert(111,0,200,0x200);
            // pctInsert(444,130,200,0x200);
            // pctInsert(333,50,100,0x800);

            std::ifstream MyReadFile(fname);
            std::string line;
            while( getline(MyReadFile, line) ) {
                if( line.at(0)=='#' ) continue;

                uint32_t v[4];
                for(int i=0; i<4; i++ ) {
                    int f = line.find(';');
                    int base = i!=3 ? 10 : 16;
                    v[i] = std::stoi(line.substr(0,f), nullptr, base);
                    line = line.substr(f+1);
                }
                pctInsert(v[0],v[1],v[2],v[3]);
            }
            MyReadFile.close();

            // throw Exception(ENOSYS, __func__);
        }

// ================================================================================== //

    } // end of namespace group

} // end of namespace somm22

