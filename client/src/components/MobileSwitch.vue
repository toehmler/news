<template>
  <div class="my-8 flex flex-row justify-center items-center select-none">
    <div class="flex flex-row mr-5">
      <img 
        v-if="!toggleState"
        v-for="(source, idx) in leftSources"
        :key="idx"
        class="w-12 h-12 rounded-xl mx-3"
        :src="source[3]">
      <img 
        v-if="toggleState"
        v-for="(source, idx) in rightSources"
        :key="idx"
        class="w-12 h-12 rounded-xl mx-3"
        :src="source[3]">
    </div>
    <VueToggles
      :value="toggleState"
      checkedBg="red"
      uncheckedBg="blue"
      @click="toggleClick"
    />
  </div>
</template>


<script>
import VueToggles from 'vue-toggles';

export default {
  props: {
    leftSources: {
      type: Array,
      required: true,
    },
    rightSources: {
      type: Array,
      required: true,
    },
    toggleState: {
      type: Boolean,
      required: true
    }
  },
  methods: {
    toggleClick() {
      this.$emit('toggleClick');
    }
  },
  components: {
    VueToggles
  }
}
</script>




