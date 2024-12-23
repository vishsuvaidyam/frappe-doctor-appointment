<template>
    <div class="w-full px-40 pt-10">
        <h1 class="text-2xl font-bold text-center text-gray-400">ABOUT <span class="text-md text-black">US</span>
        </h1>
        <div class="w-full flex justify-center pt-10">
            <div class="w-[20%]">
                <img src="../assets/about_image-MG9zrc7b.png" />
            </div>
            <div class="w-[80%] flex items-center justify-center">
                <div class="   px-20 ">
                    <p class="pb-6 text-sm text-gray-500 font-normal text-justify">Welcome to Prescripto, your trusted
                        partner in managing your healthcare needs conveniently and
                        efficiently. At Prescripto, we understand the challenges individuals face when it comes to
                        scheduling doctor appointments and managing their health records.</p>
                    <p class="pb-6 text-sm text-gray-500 font-normal text-justify">Prescripto is committed to excellence
                        in healthcare technology. We continuously strive to enhance
                        our
                        platform, integrating the latest advancements to improve user experience and deliver superior
                        service. Whether you're booking your first appointment or managing ongoing care, Prescripto is
                        here
                        to support you every step of the way.</p>
                    <h1 class="pb-6 text-sm text-black font-semibold text-justify">Our Vision</h1>
                    <p class="pb-6 text-sm text-gray-500 font-normal text-justify">Our vision at Prescripto is to create
                        a seamless healthcare experience for every user. We aim to
                        bridge the gap between patients and healthcare providers, making it easier for you to access the
                        care you need, when you need it.</p>
                </div>
            </div>
        </div>

        <div class="w-full pt-10">
            <h1 class="text-lg font-semibold pb-4">WHY <span class="text-lg font-extrabold text-gray-500">CHOOSE
                    US</span></h1>
            <div class="flex justify-center">
                <div class="w-1/3 h-56 border flex items-center justify-center hover:bg-blue-600 hover:text-white">
                    <div class="px-20">
                        <h1 class="text-md font-bold text-slate-500 pb-6">EFFICIENCY:</h1>
                        <h5 class="text-sm font-normal text-slate-500">Streamlined appointment scheduling that fits into
                            your busy lifestyle.</h5>
                    </div>
                </div>
                <div class="w-1/3 h-56 border flex items-center justify-center hover:bg-blue-600 hover:text-white">
                    <div class="px-20">
                        <h1 class="text-md font-bold text-slate-500 pb-6">CONVENIENCE:</h1>
                        <p class="text-sm font-normal text-slate-500"> Access to a network of trusted healthcare
                            professionals in your area.</p>
                    </div>
                </div>
                <div class="w-1/3 h-56 border flex items-center justify-center hover:bg-blue-600 hover:text-white">
                    <div class="px-20">
                        <h1 class="text-md font-bold text-slate-500 pb-6">PERSONALIZATION:</h1>
                        <p class="text-sm font-normal text-slate-500"> Tailored recommendations and reminders to help
                            you stay on top of your health</p>
                    </div>
                </div>

            </div>
        </div>
        <div class="mt-20">
            <Footer />
        </div>
    </div>

</template>
<script setup>
import Footer from '../components/Footer.vue';
</script>
