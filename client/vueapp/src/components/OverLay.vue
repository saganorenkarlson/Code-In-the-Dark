<!-- overlay.vue -->
<script setup>
import { useOverlayMeta } from 'unoverlay-vue'


// Define the events used in the component(optional)
// This allows you to use hints in components
//defineEmits(['cancel', 'confirm'])

// Get Overlay information from useOverlayMeta
const { visible } = useOverlayMeta({
  // Animation duration to avoid premature destruction of components
  // Only use component in template and no need to define
  animation: 1000
})
</script>

<template>
  <div v-if="visible" @click="confirm(`${title}:confirmed`)">
    HEEEEj  </div>
</template>