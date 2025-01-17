<!-- <template>
  <div class="max-w-4xl mx-auto p-6">
    
    <div class="bg-white shadow-lg rounded-lg overflow-hidden">
     
      <div class="relative bg-blue-500 p-6 text-white">
        <div class="flex justify-center items-center">
          <img
            class="w-24 h-24 rounded-full border-4 border-white -mt-2"
            :src="user.profileImage"
            :alt="user.name"
          />
        </div>
        <div class="mt-4 text-center">
          <h2 class="text-xl font-semibold">{{ user.name }}</h2>
          <p class="text-sm">{{ user.status }}</p>
        </div>
      </div>

      
      <div class="p-6 space-y-4">
        <div>
          <h3 class="font-semibold text-gray-700">About</h3>
          <p class="text-gray-600">{{ user.bio }}</p>
        </div>

        <div>
          <h3 class="font-semibold text-gray-700">Contact Information</h3>
          <p class="text-gray-600">
            <strong>Email: </strong>{{ user.email }}
          </p>
          <p class="text-gray-600">
            <strong>Phone: </strong>{{ user.phone }}
          </p>
        </div>

        <div>
          <h3 class="font-semibold text-gray-700">Location</h3>
          <p class="text-gray-600">{{ user.location }}</p>
        </div>
      </div>

      
      <div class="bg-gray-100 p-4 text-center">
        <button class="bg-blue-500 text-white px-4 py-2 rounded-lg hover:bg-blue-600 transition">
          Edit Profile
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>

const user = {
  name: 'Vivek Kumar',
  status: 'Available',
  profileImage: 'https://via.placeholder.com/150',
  bio: 'A passionate developer with a love for technology and coding.',
  email: 'vivek@123gmail.com',
  phone: '+91 9876543212',
  location: 'Chhapra,Saran Bihar',
};
</script>

<style scoped>
</style> -->


<!-- <template>
  <div class="w- full h-screen">
    <div class="bg-white h-auto w-200 shadow-md rounded-lg p-6">
      <div class="text-sm text-gray-500 mb-4">
        <a href="#" class="hover:underline">People</a> / <span>Vishwajeet Kumar</span>
      </div>

      <div class="flex items-center space-x-4 mb-6">
        <div class="w-16 h-16 bg-gray-300 rounded-full overflow-hidden">
          <img src="https://via.placeholder.com/150" alt="Profile" class="w-full h-full object-cover">
        </div>
        <h1 class="text-2xl font-bold text-gray-800">Vishwajeet Kumar</h1>
      </div>
      <div class="flex space-x-4 border-b mb-4">
        <button class="pb-2 border-b-2 border-gray-800 text-gray-800 font-medium">About</button>
        <button class="pb-2 text-gray-500 hover:text-gray-800">Certificates</button>
      </div>
      <div class="text-gray-500">
        <h2 class="text-lg font-semibold">Certificates</h2>
        <p>No certificates available.</p>
      </div>
      <div class="mt-6 text-right">
        <button class="px-4 py-2 bg-gray-800 text-white rounded hover:bg-gray-700">Edit Profile</button>
      </div>
    </div>
  </div>

</template> -->

<template>

  <div class="h-screen">
    <div class="text-sm text-gray-500 mb-4">
      <a href="#" class="hover:underline">People</a> / <span>Vivek Kumar</span>
    </div>
    <div class="bg-[#f3f3f3]  h-40"></div>
    <div class="flex  justify-center items-center gap-10 -mt-20">
      <div
        class="w-28 h-28 rounded-full bg-[#f3f3f3] flex items-center justify-center text-2xl font-bold text-gray-600 border-4 border-white mt-16 ">
        <img v-if="userImage" :src="userImage" alt="Profile" class=" w-24 h-24 border bg-white p-1  object-cover rounded-full" />
          <div v-else class=" w-24 h-24 flex items-center justify-center rounded-full">
            <span class="text-lg font-semibold text-gray-700">{{ full_name[0] }}</span>
          </div>
      </div>
     
     <div class="flex gap-60  mt-14">
      <div class="flex">
        <span class="mt-4 text-lg font-semibold text-gray-700">{{ full_name }}</span>
      </div>
      <div class="">
        <button class="mt-3 px-3 py-1 text-sm border bg-[#f3f3f3]  text-black rounded-md ">
          Edit Profile
        </button>
      </div>
     </div>
    </div>
  </div>

</template>
<script setup>
import { ref,onMounted } from 'vue';
const userImage = ref(null);
const full_name = ref('')

onMounted(() => {
  const storedData = sessionStorage.getItem("user");
  if (storedData) {
    const userData = JSON.parse(storedData);
    userImage.value = userData?.user_image;
    full_name.value = userData?.full_name;
  }
});
</script>