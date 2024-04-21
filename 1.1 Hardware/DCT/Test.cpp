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
    ap_fixed<32, 12> counter = 0;


    // Dummy coefficients for testing


    // Process each packet
    while (1)
    {
        // Read input packet
        A.read(tmp);

        counter++;




        B.write(tmp.data * (!(counter & 1) ? 125 : 1767766953));

        // Break out of the loop if it's the last packet
        if (tmp.last)
        {
            break;
    }


    }


}
