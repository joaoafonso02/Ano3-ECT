
/*
 *  \author Pedro Durval
 */

#include "somm22.h"
#include "sim_module.h"
#include <string.h>

#include <string>
#include <fstream>
#include <iostream>

namespace somm22
{

    namespace group
    {

// ================================================================================== //

        bool simCheckInputFormat(const char *fname)
        {
            soProbe(502, "%s(\"%s\")\n", __func__, fname);

            // TODO

            FILE *f = fopen(fname, "r");
            if (f == NULL)
                return false;

            char line[1024];
            char *p;
            uint32_t line_count = 0;
            while ((p = fgets(line,1024,f)) != NULL){
                
                // check if line is a comment
                if(p[0] == '#'){
                    continue;
                }

                line_count++;

                // clear whitespaces
                uint32_t count = 0;
                for(uint32_t i = 0; p[i]; i++){
                    if((p[i] != ' ') & (p[i] != '\t')){
                        p[count++] = p[i];
                    }
                }
                p[count] = '\0';

                // save for later prints only
                char second[1024]; 
                strcpy(second,p);

                // split string by ';'
                char *tok = strtok(p,";");
                uint32_t size = 0;
                
                // verify if pid is not 0 and determine ammount of fields
                do{
                    if((size == 0) & (std::stoi(tok,nullptr,10) <= 0)){
                        return false;
                    }

                    // verify syntax of fields
                    if(size == 3){
                        for (uint32_t i = 2; p[i]; i++){
                            if(std::isdigit(tok[i]) == 0){
                                printf("-- Syntax error at line %d: %s",line_count,second);
                                return false;
                            }
                        }
                    }else{
                        for (uint32_t i = 0; tok[i]; i++){
                            if(std::isdigit(tok[i]) == 0){
                                printf("-- Syntax error at line %d: %s",line_count,second);
                                return false;
                            }
                        }
                    }
                
                    size += 1;
                    tok = strtok(NULL,";");
                } while(tok);
               
               // assert number of fields if 4 as expected
                if(size != 4){
                    return false;
                }
            }
            
            fclose(f);

            return true;
        }

// ================================================================================== //

    } // end of namespace group

} // end of namespace somm22