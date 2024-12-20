<template>
    <div>
        <!-- Check if there are doctors -->
        <div v-if="doctors && doctors.length > 0" 
            class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-5 gap-6 w-full">
            <div v-for="doctor in doctors" :key="doctor.full_name" 
                @click="$emit('doctorClicked', doctor)" 
                class="bg-white shadow-md rounded-lg border-t-4 border-blue-500 p-6 text-start cursor-pointer">
                <div>
                    <img class="w-full h-54 mx-auto" :src="doctor.doctor_image" :alt="doctor.full_name" />
                </div>
                <div class="mt-4">
                    <span :class="doctor.status === 'Available' ? 'text-green-500' : 'text-red-500'"
                        class="text-sm font-medium">
                        ● {{ doctor.status }}
                    </span>
                    <h3 class="text-lg font-semibold text-gray-800 mt-2">
                        {{ doctor.full_name }}
                    </h3>
                    <p class="text-sm text-gray-600">{{ doctor.specialist }}</p>
                </div>
            </div>
        </div>
        <!-- Fallback message if no doctors are available -->
        <div v-else class="text-gray-500 text-center">
            No related doctors found.
        </div>
    </div>
</template>

<script>
export default {
    props: {
        doctors: {
            type: Array,
            required: true,
        },
    },
};
</script>
