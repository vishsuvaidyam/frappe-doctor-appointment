<template>
    <div v-if="selectcity" class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center">
          <div class="bg-white p-6 rounded-lg shadow-lg max-w-4xl w-full">
            <h2 class="text-sm font-semibold mb-2 text-[#224855]">Popular cities</h2>
            <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-8 gap-2">
              <div v-for="(city, index) in resultcity" :key="index" class="flex flex-col items-center">
                <div
                  class="w-24 h-20 flex justify-center items-center rounded p-4 mt-2 border-white border-2 delay-100 transition-all hover:border-[#224855] hover:border-2"
                  :class="{ 'bg-[#fde7ac] border-yellow-500': selectedCity === city.city_name, 'bg-[#f1f7f7]': selectedCity !== city.city_name }"
                  @click="selectCity(city)">
                  <img class="w-full h-full object-cover" src="../assets/ahmedabad.svg" alt="city.name[0]" />
                </div>
                <p class="mt-2 text-center text-[#c4c2c] text-[12px] font-semibold">{{ city.city_name }}</p>
              </div>
            </div>
            <div class="mt-4 flex justify-end">
              <button class="px-4 py-2 bg-[#224855] text-white rounded hover:bg-[#3a7b91]" @click="togglecity">
                X
              </button>
            </div>
          </div>
        </div>
</template>
<script setup>
const selectcity = ref(false)
const selectedCity = ref(null)


const selectCity = async (city) => {
  selectedCity.value = city.city_name;
  console.log(city);
  
  try {
    const response = await axios.get("/api/method/appointments_management.controllers.api.get_doctors_by_city", {
      params: { town_name: city.city_name }   
    });

    resultcity = response.data.message;  
    console.log(resultcity);  
  } catch (error) {
    console.error("Error fetching city data:", error);
  }
  togglecity();
};

</script>