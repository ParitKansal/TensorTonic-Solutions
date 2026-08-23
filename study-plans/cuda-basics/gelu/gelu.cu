#include <cuda_runtime.h>
#include <math.h>

__global__ void k_fun(float* k) {
    if (blockIdx.x == 0 && threadIdx.x == 0) {
        *k = sqrtf(2.0f / 3.14159265358979323846f);
    }
}

__global__ void gelu_kernel(const float* input, float* output, const float* k, int N) {
    int idx = blockIdx.x * blockDim.x + threadIdx.x;

    if (idx < N) {
        float x = input[idx];
        output[idx] = 0.5f * x *
            (1.0f + tanhf((*k) * (x + 0.044715f * x * x * x)));
    }
}

extern "C" void solve(const float* input, float* output, int N) {
    int threads = 256;
    int blocks = (N + threads - 1) / threads;

    float* d_k;
    cudaMalloc(&d_k, sizeof(float));

    k_fun<<<1, 1>>>(d_k);
    gelu_kernel<<<blocks, threads>>>(input, output, d_k, N);

    cudaDeviceSynchronize();

    cudaFree(d_k);
}