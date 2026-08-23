#include <cuda_runtime.h>
#include <math.h>

__global__ void max_kernel(const float* input, float* max_val, int N) {
    if (blockIdx.x == 0 && threadIdx.x == 0) {
        float mx = input[0];
        for (int i = 1; i < N; i++) {
            if (input[i] > mx)
                mx = input[i];
        }
        *max_val = mx;
    }
}

__global__ void exp_kernel(const float* input, float* output, const float* max_val, int N) {
    int idx = blockIdx.x * blockDim.x + threadIdx.x;
    if (idx < N){
        output[idx] = expf(input[idx] - *max_val);
    }
}

__global__ void sum_kernel(const float* input, float* sum, int N) {
    if (blockIdx.x == 0 && threadIdx.x == 0) {
        float s = 0.0f;
        for (int i = 0; i < N; i++){
            s += input[i];
        }
        *sum = s;
    }
}

__global__ void normalize_kernel(float* output, const float* sum, int N) {
    int idx = blockIdx.x * blockDim.x + threadIdx.x;
    if (idx < N){
        output[idx] /= *sum;
    }
}

extern "C" void solve(const float* input, float* output, int N) {
    int threads = 256;
    int blocks = (N + threads - 1) / threads;

    float *d_max, *d_sum;
    cudaMalloc(&d_max, sizeof(float));
    cudaMalloc(&d_sum, sizeof(float));

    max_kernel<<<1, 1>>>(input, d_max, N);
    exp_kernel<<<blocks, threads>>>(input, output, d_max, N);
    sum_kernel<<<1, 1>>>(output, d_sum, N);
    normalize_kernel<<<blocks, threads>>>(output, d_sum, N);

    cudaDeviceSynchronize();

    cudaFree(d_max);
    cudaFree(d_sum);
}