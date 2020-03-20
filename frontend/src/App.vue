<template>
  <body>
     <main>
      <transition name="component-fade" mode="out-in">
        <router-view />
      </transition>
    </main>
  </body>
</template>

<script>

export default {
  name: 'App',
}
</script>

<style>

</style>
