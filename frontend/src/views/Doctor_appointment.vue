<script setup>
import { ref } from 'vue';
import axios from 'axios';

// Props for doctor data
const props = defineProps({
  doctor: {
    type: Object,
    required: true,
  },
});

// Reactive state variables
const patientName = ref('');
const appointmentDate = ref('');
const appointmentTime = ref('');
const successMessage = ref('');
const errorMessage = ref('');

// Book Appointment Function
const bookAppointment = async () => {
  if (!props.doctor || !props.doctor.name) {
    errorMessage.value = 'Doctor information is missing.';
    return;
  }

  // Validate form inputs
  if (!patientName.value || !appointmentDate.value || !appointmentTime.value) {
    errorMessage.value = 'Please fill in all required fields.';
    return;
  }

  try {
    const response = await axios.post('/api/method/appointments_management.controllers.api.create_appointment', {
      doctor_name: props.doctor.name,
      patient_name: patientName.value,
      appointment_date: appointmentDate.value,
      appointment_time: appointmentTime.value,
    });

    if (response.data.message) {
      successMessage.value = response.data.message;
      errorMessage.value = '';
      resetForm();
    }
  } catch (error) {
    console.error('Error booking appointment:', error);
    errorMessage.value = 'Failed to book the appointment. Please try again.';
  }
};

// Reset Form Fields
const resetForm = () => {
  patientName.value = '';
  appointmentDate.value = '';
  appointmentTime.value = '';
};
</script>

<template>
  <div class="max-w-md mx-auto bg-white shadow-md rounded px-8 py-6">
    <h2 class="text-xl font-bold mb-4 text-gray-800">Book an Appointment</h2>
    <form @submit.prevent="bookAppointment">
      <div class="mb-4">
        <label for="patient-name" class="block mb-1 font-medium text-gray-700">Patient Name</label>
        <input
          id="patient-name"
          v-model="patientName"
          type="text"
          placeholder="Enter Patient's Name"
          class="w-full border px-4 py-2 rounded focus:outline-none focus:ring focus:ring-blue-300"
        />
      </div>
      <div class="mb-4">
        <label for="appointment-date" class="block mb-1 font-medium text-gray-700">Appointment Date</label>
        <input
          id="appointment-date"
          v-model="appointmentDate"
          type="date"
          class="w-full border px-4 py-2 rounded focus:outline-none focus:ring focus:ring-blue-300"
        />
      </div>
      <div class="mb-4">
        <label for="appointment-time" class="block mb-1 font-medium text-gray-700">Appointment Time</label>
        <input
          id="appointment-time"
          v-model="appointmentTime"
          type="time"
          class="w-full border px-4 py-2 rounded focus:outline-none focus:ring focus:ring-blue-300"
        />
      </div>
      <button
        type="submit"
        class="w-full bg-blue-600 text-white px-6 py-2 rounded shadow hover:bg-blue-700 transition duration-200"
      >
        Book Appointment
      </button>
    </form>
    <p v-if="successMessage" class="mt-4 text-green-500">{{ successMessage }}</p>
    <p v-if="errorMessage" class="mt-4 text-red-500">{{ errorMessage }}</p>
  </div>
</template>
