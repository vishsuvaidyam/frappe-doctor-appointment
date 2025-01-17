<template>
  <div class="h-screen">
    <div class="text-sm text-gray-500 py-2">
      <a href="#" class="hover:underline text-lg font-semibold ">People</a> / <span class="text-lg font-semibold text-gray-700">{{ full_name }}</span>
    </div>
    <div class="bg-[#f3f3f3]  h-40"></div>
    <div class="flex  justify-center items-center gap-10 -mt-20">
      <div
        class="w-28 h-28 rounded-full bg-[#f3f3f3] flex items-center justify-center text-2xl font-bold text-gray-600 border-4 border-white mt-16 ">
        <img v-if="userImage" :src="userImage" alt="Profile" class=" w-24 h-24 border bg-white p-1  object-cover rounded-full" />
          <div v-else class=" w-24 h-24 flex items-center justify-center rounded-full">
            <span class="text-lg  text-[#aaa9b6]">{{ full_name[0] }}</span>
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