<template>
  <body>
    <div class="full-control">
    <div class="list">

      <md-list v-for="item in themes" :key="item.id">
        <md-list-item md-expand :md-expanded.sync="item.expand">
          <span class="md-list-item-text">{{item.name}}</span>

          <md-list slot="md-expand">
            <md-list-item class="md-inset" v-for="subtopic in item.subtopics" :key="subtopic.id" @click=gotoinfo(subtopic.link)>
              {{ subtopic.name }}
            </md-list-item>
          </md-list>
        </md-list-item>

      </md-list>
    </div>
  </div>

  </body>
</template>

<script>

export default {
  name: 'Startpage',

  data: function() {
    return {
      themes: [
        {name: "Persönliche Gesundheit", id: 1, expand: false, subtopics: [
                                                                {name: "Habe ich Corona?", id: 11, link: "/medical"}, 
                                                                {name: "Ich habe Corona, was sollte ich tun?", id: 12, link: "/medical"}, 
                                                                {name: "Wo bekomme ich Hilfe bei psychischen Problemen?", id: 13, link: "/mentalhealth"}]}, 
        {name: "Rechtliche Informationen", id: 2, expand: false, subtopics: [
                                                                {name: "Darf ich noch raus?", id: 21, link: "/legal"}, 
                                                                {name: "Woher bekomme ich finanzielle Unterstützung?", id: 22, link: "/legal"}]}, 
        {name: "Informationen zum Virus", id: 3, expand: false, subtopics: [
                                                                {name: "Was ist das für ein Virus?", id: 31, link: "/virus"}, 
                                                                {name: "Was wird aktuell geforscht?", id: 32, link: "/virus"}, 
                                                                {name: "Wie ist die Ausbreitung?", id: 33, link: "/virus"}]}, 
        ],
        // Nachbarschafts Hilfe wo bekommen, wo anbieten?
    }
  },

  methods: {
    gotoinfo: function(link){
      this.$router.push(link); 
    }
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