<template>
  <body>
    <div class="full-control">
      <div class="list">

        <md-list v-for="faq in faqs" :key="faq.question">
          <md-list-item md-expand>
                {{ faq.answer}}
          </md-list-item>

        </md-list>
      </div>
  </div>

  </body>
</template>

<script>
import Api from "../api.js";

export default {
  name: 'FaqPage',

  data: function() {
    return {
      faqs: [],
    }
  },

  methods: {
    gotoinfo: function(link){
      this.$router.push(link); 
    }
  },

  mounted(){
    Api.get(`/faqs/get_all_faqs`)
    .then(response => {
      this.faqs = response.data.faqs;
    }, error => {
      console.error(error);
    });
  },


}
</script>

<style lang="scss" scoped>
  $list-width: 100%;

  .full-control {
    display: flex;
    flex-direction: row;
    flex-wrap: wrap-reverse;
  }

  .list {
    width: $list-width;
  }

  .md-list {
    width: 100%;
    max-width: 100%;
    display: inline-block;
  }

  .full-control > .md-list {
    width: $list-width;
    max-width: 100%;
    height: 400px;
    display: inline-block;
    overflow: auto;
    border: 1px solid rgba(#000, .12);
    vertical-align: top;
  }

  .control {
    min-width: 250px;
    display: flex;
    flex-direction: column;
    padding: 16px;
  }
</style>