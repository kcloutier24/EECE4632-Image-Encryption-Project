#include "ap_axi_sdata.h"
#include "hls_stream.h"

#define DCT_SIZE 8 // Change this to your desired DCT size
typedef short dct_data_t;

void dct(hls::stream<ap_axis<32, 2, 5, 6>> &input_stream, hls::stream<ap_axis<32, 2, 5, 6>> &output_stream)
{
    // Internal buffers

#pragma HLS INTERFACE axis port = input_stream
#pragma HLS INTERFACE axis port = output_stream
#pragma hls interface s_axilite port = return
    dct_data_t in_block[DCT_SIZE][DCT_SIZE];
    dct_data_t out_block[DCT_SIZE][DCT_SIZE];

    // Read input data from stream
    for (int r = 0; r < DCT_SIZE; r++)
    {
        for (int c = 0; c < DCT_SIZE; c++)
        {
            ap_axis<32, 2, 5, 6> val = input_stream.read();
            in_block[r][c] = val.data;
        }
    }

    // Perform 2D DCT
    unsigned int k, n;

    int tmp;
    const dct_data_t dct_coeff_table[DCT_SIZE][DCT_SIZE] = {
        8192, 8192, 8192, 8192, 8192, 8192, 8192, 8192,
        11363, 9633, 6436, 2260, -2260, -6436, -9632, -11362,
        10703, 4433, -4433, -10703, -10703, -4433, 4433, 10703,
        9633, -2260, -11362, -6436, 6436, 11363, 2260, -9632,
        8192, -8192, -8192, 8192, 8192, -8191, -8191, 8192,
        6436, -11362, 2260, 9633, -9632, -2260, 11363, -6436,
        4433, -10703, 10703, -4433, -4433, 10703, -10703, 4433,
        2260, -6436, 9633, -11362, 11363, -9632, 6436, -2260

    };

    // DCT rows
    for (k = 0; k < DCT_SIZE; k++)
    {
        for (n = 0; n < DCT_SIZE; n++)
        {
            int coeff = (int)dct_coeff_table[k][n];
            tmp = 0;
            for (unsigned int i = 0; i < DCT_SIZE; i++)
            {
                tmp += in_block[n][i] * coeff;
            }
            out_block[k][n] = tmp;
        }
    }

    // Write output data to stream
    for (int r = 0; r < DCT_SIZE; r++)
    {
        for (int c = 0; c < DCT_SIZE; c++)
        {
            ap_axis<32, 2, 5, 6> val;
            val.data = out_block[r][c];
            val.keep = 1;
            val.strb = 1;
            val.last = (r == DCT_SIZE - 1 && c == DCT_SIZE - 1) ? 1 : 0;
            output_stream.write(val);
        }
    }
}
