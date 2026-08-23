#include <cuda_runtime.h>
#include <math.h>

__global__ void gelu_kernel(const float* input, float* output, int N) {
    // Write code here
    int idx = blockIdx.x * blockDim.x + threadIdx.x;
    if(idx < N){
        float x = input[idx];
        output[idx] = 0.5f * x *(1.0f + tanhf(
            0.7978845608f *(x + 0.044715f * x*x*x)
        ));
    }
}

extern "C" void solve(const float* input, float* output, int N) {
    int threads = 256;
    dim3 blocks((N + 255) / 256);
    gelu_kernel<<<blocks, threads>>>(input, output, N);
    cudaDeviceSynchronize();
}
