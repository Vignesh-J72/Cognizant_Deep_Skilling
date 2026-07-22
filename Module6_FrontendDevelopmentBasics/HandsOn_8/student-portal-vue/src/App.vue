<template>
  <div class='app-container'>
    <Header />
    <main>
      <RouterView />
    </main>
  </div>
</template>

<script setup>
import {RouterView} from 'vue-router';
import Header from '@/components/Header.vue';
</script>