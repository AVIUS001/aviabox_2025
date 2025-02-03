// simulation/nvidia_technologies/cuda/kernels/sensor_data_processing.cu
#include <stdio.h>

__global__ void processSensorData(double* data, int n) {
    int i = blockIdx.x * blockDim.x + threadIdx.x;
    if (i < n) {
        data[i] = data[i] * 2.0;
    }
}

extern "C" void runSensorKernel(double* data, int n) {
    processSensorData<<<(n+255)/256, 256>>>(data, n);
}
