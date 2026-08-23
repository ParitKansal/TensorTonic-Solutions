#include <cuda_runtime.h>

__global__ void matrix_add_kernel(const float* A, const float* B, float* C, int M, int N) {

    // Column index
    int col = blockIdx.x * blockDim.x + threadIdx.x;

    // Row index
    int row = blockIdx.y * blockDim.y + threadIdx.y;

    // Check that the thread is inside the matrix
    if (row < M && col < N) {

        // Convert 2D index to 1D index
        int idx = row * N + col;

        C[idx] = A[idx] + B[idx];
    }
}


extern "C" void solve(const float* A, const float* B, float* C, int M, int N) {
    dim3 threads(16, 16);
    dim3 blocks((N + 15) / 16, (M + 15) / 16);
    matrix_add_kernel<<<blocks, threads>>>(A, B, C, M, N);
    cudaDeviceSynchronize();
}
