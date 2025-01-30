<template>
  <!-- <div class="w-full  py-10 bg">
    <div class="bg-[#367892] h-auto flex flex-col lg:flex-row items-center rounded-lg  mx-4 sm:mx-6 md:mx-10 lg:mx-20">
      <div class="container mx-auto px-4 sm:px-6 md:px-8 py-6">
        <div class="flex flex-col lg:flex-row items-center">
          <div class="lg:w-1/2 text-center lg:text-left pb-8 lg:pb-0">
            <h1 class="text-3xl sm:text-4xl md:text-5xl font-bold text-white pb-4">
              Book Appointment <br />
              With Trusted Doctors
            </h1>
            <div class="flex flex-col sm:flex-row items-center sm:items-start space-y-4 sm:space-y-0 sm:space-x-4 pb-6">
              <div class="flex -space-x-4">
                <img class="w-8 sm:w-10 h-8 sm:h-10 rounded-full border-2 border-white" src="../assets/logo.jpg" alt="Person 1" />
                <img class="w-8 sm:w-10 h-8 sm:h-10 rounded-full border-2 border-white" src="../assets/logo.jpg" alt="Person 2" />
                <img class="w-8 sm:w-10 h-8 sm:h-10 rounded-full border-2 border-white" src="../assets/logo.jpg" alt="Person 3" />
              </div>
              <p class="text-white text-sm sm:text-base px-4">
                Simply browse through our extensive list of trusted doctors, schedule your appointment hassle-free.
              </p>
            </div>
            <a href="#"
              class="inline-flex items-center bg-white text-gray-500 text-sm font-semibold py-2 px-4 sm:py-3 sm:px-6 rounded-3xl shadow-lg hover:scale-105 transition-all">
              Book appointment
              <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" class="ml-2" viewBox="0 0 24 24">
                <path fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round"
                  stroke-miterlimit="10" stroke-width="1.5" d="m14 16l4-4m0 0l-4-4m4 4H6" />
              </svg>
            </a>
          </div>
          <div class="lg:w-1/2 flex justify-center mt-6 lg:mt-0">
            <img class="w-full max-w-sm md:max-w-md lg:max-w-full" src="../assets/header_img-DhAi3lLA.png" alt="Doctors" />
          </div>
        </div>
      </div>
    </div>

    <div>
      <Speciality />
    </div>

    <div class="mx-4 sm:mx-6 md:mx-10 lg:mx-20 pt-10">
      <div class="text-center">
        <h2 class="text-xl sm:text-2xl md:text-3xl font-bold text-gray-800">Top Doctors to Book</h2>
        <p class="text-gray-800 mt-2">Simply browse through our extensive list of trusted doctors.</p>
      </div>
      <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-5 gap-4 sm:gap-6 pt-10">
        <All_doctors />
      </div>
      <div class="flex justify-center items-center pt-5">
        <router-link to="/doctors" class="px-8 py-2 rounded-3xl border bg-gray-50 text-gray-800 text-sm sm:text-base">
          More
        </router-link>
      </div>
    </div>

    <div class="bg-[#367892]  h-auto flex flex-col lg:flex-row items-center rounded-lg mt-10 mx-4 sm:mx-6 lg:mx-20 p-6">
      <div class="lg:w-1/2 text-center lg:text-left mb-6 lg:mb-0 px-4">
        <h1 class="text-2xl sm:text-3xl md:text-4xl lg:text-5xl font-bold text-white pb-4">
          Book Appointment <br> With 100+ Trusted Doctors
        </h1>
        <router-link to="/register"
          class="inline-block cursor-pointer bg-white py-2 sm:py-3 px-4 sm:px-6 rounded-3xl text-gray-500 font-semibold hover:scale-105 transition-all">
          Create Account
        </router-link>
      </div>
      <div class="lg:w-1/2 flex justify-center">
        <img class="w-full max-w-xs sm:max-w-sm md:max-w-md lg:max-w-lg object-contain rounded-lg"
          src="../assets/appointment_female.png" alt="Doctors" />
      </div>
    </div>

    <div class="mt-20">
      <Footer />
    </div>
  </div>
</div> -->
  <div class="bg-white shadow-lg font-sans py-10 mx-4 md:mx-16 lg:mx-60">

    <!-- Search Section -->
    <div class="bg-[#2e718e] py-6"></div>
    <section class="bg-[#367892] bg py-20">
      <div class="container mx-auto px-6 md:px-16 lg:px-20 text-center">
        <h1 class="text-3xl text-white font-semibold mb-4">Best Doctors In Patna</h1>
        <div class="flex flex-col md:flex-row justify-center items-center space-y-4 md:space-y-0 md:space-x-2">

          <div class="relative w-full md:w-1/2">
            <select class="w-full px-4 py-2 pl-10 rounded-md outline-none border border-gray-300 appearance-none" />
            <i class="fa fa-search absolute  left-3 top-1/2 transform -translate-y-1/2" aria-hidden="true"></i>
          </div>
          <div class="relative md:w-1/2">
            <img class="w-4 h-4 absolute left-3 top-1/2 transform -translate-y-1/2 pointer-events-none"
              src="../assets/icons8-location-50.png" alt="">
            <select
              class="w-full px-10 py-2 rounded-md text-sm outline-none text-[#224855] border border-gray-300 appearance-none">
              <option class="text-sm text-[#224855]">Select Hospital</option>
              <option class="text-sm text-[#224855]">Hospital 1</option>
              <option class="text-sm text-[#224855]">Hospital 2</option>
            </select>
            <!-- <span class="absolute right-3 top-1/2 transform -translate-y-1/2 pointer-events-none">
              <i class="fa fa-caret-down  h-2 text-[#224855]" aria-hidden="true"></i>
            </span> -->
          </div>


        </div>
      </div>
    </section>
    <main class="container mx-auto px-4 py-8">
      <div class="flex flex-col gap-8 justify-center sm:flex-row sm:gap-4 md:gap-6 lg:gap-8 mb-6">
        <!-- Filter Section -->
        <div class="w-full sm:w-3/4 lg:w-2/3">
          <div class="flex flex-wrap gap-2 p-2">
            <!-- Filter Button -->
            <button class="flex items-center space-x-2 px-4 py-2 text-[#224855] border border-[#224855] rounded-md">
              <i class="fa fa-filter text-[#224855]" aria-hidden="true"></i>
              <span>Filter</span>
            </button>

            <!-- Dropdowns -->
            <select v-model="activeSpecialist" @change="fetchDoctors"
              class="px-4 py-2 rounded-md text-sm border border-[#224855] text-[#224855] bg-transparent outline-none">
              <option value="">Speciality</option>
              <option class="option-class" v-for="specialist in specialists" :key="specialist.name1"
                :value="specialist.name1">
                {{ specialist.name1 }}
              </option>
            </select>

            <select v-if="doctors.length > 0" v-model="selectedGender" @change="fetchDoctors"
              class="px-4 py-2 rounded-md text-sm border border-[#224855] text-[#224855] bg-transparent outline-none">
              <option value="">Gender</option>
              <!-- Loop through unique genders -->
              <option v-for="gender in uniqueGenders" :key="gender" :value="gender">{{ gender }}</option>
            </select>

            <select
              class="px-4 py-2 rounded-md text-sm border border-[#224855] text-[#224855] bg-transparent outline-none">
              <option>Language</option>
            </select>
            <select
              class="px-4 py-2 rounded-md text-sm border border-[#224855] text-[#224855] bg-transparent outline-none">
              <option>Sort</option>
            </select>
          </div>

          <h2 v-if="doctors.length > 0" class="text-md font-bold text-[#224855] py-4">
            Search Result ({{ doctors.length }})
          </h2>

          <div v-for="doctor in doctors" :key="doctor.full_name">
            <div
              class="bg-white rounded-lg shadow-md px-4 py-8 mb-4 flex flex-col sm:flex-row items-center border border-gray-200">
              <img :src="doctor.doctor_image" :alt="doctor.full_name[0]" alt="Doctor"
                class="h-20 w-20 rounded-full border-2 border-gray-300">
              <div class="mt-4 sm:mt-0 sm:ml-4 px-2 text-center sm:text-left">
                <h3 class="text-md font-bold text-[#224855]">{{ doctor.full_name }}</h3>
                <p class="text-[12px] font-normal text-[#367892] border-b py-2">
                  {{ doctor.specialist }} | {{ doctor.experience }}
                </p>
                <p class="text-sm text-gray-500 py-2 flex gap-1 justify-center sm:justify-start">
                  <img class="w-4 h-4" src="../assets/icons8-location.gif" alt="">
                  {{ doctor.address }}
                </p>
                <p class="text-sm flex gap-2 text-gray-500 justify-center sm:justify-start">
                  <img src="https://www.askapollo.com/assets/images/language.svg" alt="">
                  {{ doctor.language }}
                </p>
                <p class="text-sm flex gap-2 text-gray-500 justify-center sm:justify-start">
                  <img src="https://www.askapollo.com/assets/images/qualification.svg" alt="">
                  {{ doctor.qulifications }}
                </p>
              </div>
              <div v-if="doctor.shifts && doctor.shifts.length > 0" class="mt-4 sm:mt-0 sm:ml-auto text-right">
                <p class="text-sm font-semibold text-green-600">MON - SAT</p>
                <div v-for="shift in doctor.shifts" :key="shift.name">
                  <p class="text-sm text-[#03a9d9]">
                    ( {{ formatTime(shift.start_time) }} - {{ formatTime(shift.end_time) }})
                  </p>
                </div>
                <button class="bg-[#005488] text-white px-4 text-[10px] py-2 rounded-md mt-4"
                  @click="goToDoctorDetails(doctor.full_name, doctor.specialist)">
                  BOOK APPOINTMENT
                </button>
              </div>
              <div v-else class="mt-4 sm:mt-0 sm:ml-auto text-right">
                <button
                  class="bg-[#30627e] opacity-50 cursor-not-allowed text-white px-4 text-[10px] py-2 rounded-md mt-4">
                  BOOK APPOINTMENT
                </button>
              </div>
            </div>
          </div>
        </div>

        <!-- Image Section -->
        <div class="w-full sm:w-1/4 lg:w-1/4 h-auto relative">
          <div class="sticky border rounded-lg p-10 top-24">
            <img class="w-full h-full object-cover" src="../assets/need-help.svg" alt="Need Help">
          </div>
          <div class="absolute top-28 text-center font-bold left-1/2 transform -translate-x-1/2 pl-8">
            <p class="text-[#F4A100] text-sm">Need Help?</p>
            <p class="hover:text-[#F4A100] cursor-pointer">1860 500 1066</p>
          </div>
        </div>
      </div>
    </main>
    <div class="flex justify-center items-center pb-8">
      <router-link to="/doctors"
        class="px-10 py-2 font-semibold rounded-md border bg-[#125a6e] text-white text-sm sm:text-base">
        VIEW ALL
      </router-link>
    </div>
    <!-- Floating Buttons -->
    <div class="fixed bottom-4 right-4 space-y-4">
      <button class="bg-[#4849bd] text-white px-8 py-3 rounded-md shadow-md flex items-center space-x-2">
        <i class="fa fa-phone" aria-hidden="true"></i>
        <span class="text-[10px] font-semibold">BOOK APPOINTMENT</span>
      </button>
      <button class="bg-[#F4A100] text-white px-10 py-3 rounded-md shadow-md flex items-center space-x-2">
        <span class="text-[10px] font-semibold">REQUEST A CALL BACK</span>
      </button>
    </div>

  </div>

</template>

<script setup>
// import Speciality from './Speciality.vue';
// import All_doctors from './All_doctors.vue';

import axios from "axios";
import { ref, onMounted, computed } from "vue";
import { useRouter } from "vue-router";

const router = useRouter();
const doctors = ref([]);
const allDoctors = ref([]);
const specialists = ref([]);
const activeSpecialist = ref("");
const selectedGender = ref("");

// Fetch doctors data
const fetchDoctorsData = async () => {
  try {
    const response = await axios.get(
      "api/method/appointments_management.controllers.api.doctors_data"
    );
    doctors.value = response.data.message || [];
    allDoctors.value = doctors.value;
  } catch (error) {
    console.error("Error fetching doctors data:", error);
  }
};

// Fetch specialists data
const fetchSpecialists = async () => {
  try {
    const response = await axios.get(
      "api/method/appointments_management.controllers.api.spaclist"
    );
    specialists.value = response.data.message || [];
  } catch (error) {
    console.error("Error fetching specialists data:", error);
  }
};

// Filter doctors based on specialist and gender
const fetchDoctors = () => {
  doctors.value = allDoctors.value.filter((doctor) => {
    const matchesSpecialist = activeSpecialist.value
      ? doctor.specialist === activeSpecialist.value
      : true;

    const matchesGender = selectedGender.value
      ? doctor.gender === selectedGender.value
      : true; // Apply gender filter only if selectedGender is not empty

    return matchesSpecialist && matchesGender;
  });
};

// Extract unique genders from doctors
const uniqueGenders = computed(() => {
  const genders = allDoctors.value.map(doctor => doctor.gender).filter(Boolean);
  return [...new Set(genders)]; // Remove duplicates using Set
});

// Format time for shifts
const formatTime = (time) => {
  const [hour, minute] = time.split(":").map(Number);
  const period = hour >= 12 ? "PM" : "AM";
  const formattedHour = hour % 12 || 12;
  return `${formattedHour}:${minute.toString().padStart(2, "0")} ${period}`;
};

// Navigate to doctor's details page
const goToDoctorDetails = (full_name, specialist) => {
  router.push({ name: "Doctor_details", params: { full_name, specialist } });
};

// Fetch data on mount
onMounted(() => {
  fetchDoctorsData();
  fetchSpecialists();
});
</script>
<style>
.bg {
  background-image: url("../assets/directory-top-bg.svg");
  background-repeat: no-repeat;
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
}
</style>