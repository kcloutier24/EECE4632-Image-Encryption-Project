#include "ap_axi_sdata.h"
#include "hls_stream.h"

void DCT(hls::stream<ap_axis<32, 2, 5, 6>> &A, hls::stream<ap_axis<32, 2, 5, 6>> &B)
{
    // Interface directives for Vivado HLS
#pragma HLS INTERFACE axis port = A
#pragma HLS INTERFACE axis port = B
#pragma HLS interface s_axilite port = return

    ap_axis<32, 2, 5, 6> tmp;
    ap_axis<32, 2, 5, 6> result;
    int counter = 0;


        while(1)
        {
    	A.read(tmp);


    	tmp.data+=7;


    	B.write(tmp);
         if(tmp.last)
         {
             break;
         }
        }


}
