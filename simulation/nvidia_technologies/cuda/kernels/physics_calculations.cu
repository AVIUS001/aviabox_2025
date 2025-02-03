// simulation/nvidia_technologies/cuda/kernels/physics_calculations.cu
#include <stdio.h>

__global__ void computePhysics(double* positions, double dt, int n) {
    int i = blockIdx.x * blockDim.x + threadIdx.x;
    if (i < n) {
        positions[i] += dt;
    }
}

extern "C" void runPhysicsKernel(double* positions, double dt, int n) {
    computePhysics<<<(n+255)/256, 256>>>(positions, dt, n);
}
