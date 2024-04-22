
#include "ap_axi_sdata.h"
#include "hls_stream.h"

void Huff(hls::stream<ap_axis<32, 2, 5, 6>> &A, hls::stream<ap_axis<32, 2, 5, 6>> &B)
{
    // Interface directives for Vivado HLS
#pragma HLS INTERFACE axis port = A
#pragma HLS INTERFACE axis port = B
#pragma HLS INTERFACE s_axilite port = return

    ap_axis<32, 2, 5, 6> tmp;

    ap_fixed<32, 12> in_data[64];

    int index = 0; // Initialize index

    while (1)
    {
        // Read data from stream A
        A.read(tmp);

        if(tmp.data<6)
        {
        	tmp.data = tmp.data;
        }
        else
        {
        	tmp.data =  tmp.data - 5;
        }


        B.write(tmp);

        // Check if the current packet is the last one
        if (tmp.last)
        {




            break; // Break out of the loop if it's the last packet
        }
    }
}
