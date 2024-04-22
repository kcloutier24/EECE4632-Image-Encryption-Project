#include "ap_axi_sdata.h"
#include "hls_stream.h"

#define DCT_SIZE 8
typedef short dct_data_t;

void Huff(hls::stream<ap_axis<32, 2, 5, 6>>& input_stream, hls::stream<ap_axis<32, 2, 5, 6>>& output_stream) {
    dct_data_t in_block[DCT_SIZE][DCT_SIZE];
    dct_data_t out_block[DCT_SIZE][DCT_SIZE];

    #pragma HLS INTERFACE axis port = input_stream
    #pragma HLS INTERFACE axis port = output_stream
    #pragma hls interface s_axilite port = return

    int freq[256] = {0};
    int codes[256][DCT_SIZE];
    for (int i = 0; i < 256; i++) {
        for (int j = 0; j < DCT_SIZE; j++) {
            codes[i][j] = -1;
        }
    }

    // symbol frequencies
    for (int r = 0; r < DCT_SIZE; r++) {
        for (int c = 0; c < DCT_SIZE; c++) {
            ap_axis<32, 2, 5, 6> val = input_stream.read();
            in_block[r][c] = val.data;
            freq[in_block[r][c]]++;
        }
    }

    //  Huffman codes based on frequencies
    int codeLengths[256] = {0};
    int nextCode[256] = {0};
    int code = 0;
    for (int bits = 1; bits <= DCT_SIZE; bits++) {
        for (int symbol = 0; symbol < 256; symbol++) {
            if (freq[symbol] == 0) continue;
            if (codeLengths[symbol] == bits) {
                codes[symbol][codeLengths[symbol]++] = code;
                code++;
            }
        }
        code <<= 1;
    }


    for (int r = 0; r < DCT_SIZE; r++) {
        for (int c = 0; c < DCT_SIZE; c++) {
            int codeLength = codeLengths[in_block[r][c]];
            int codeValue = codes[in_block[r][c]][0];
            for (int i = 0; i < codeLength; i++) {
                ap_axis<32, 2, 5, 6> val;
                val.data = (codeValue >> (codeLength - i - 1)) & 1;
                val.keep = 1;
                val.strb = 1;
                val.last = (r == DCT_SIZE - 1 && c == DCT_SIZE - 1 && i == codeLength - 1) ? 1 : 0;
                output_stream.write(val);
            }
        }
    }
}
