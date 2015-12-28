module.exports = function(grunt) {

  // Configurable paths
  var config = {
    src: 'django-project',
    build: 'django-project/build'
  };

  // Project configuration.
  grunt.initConfig({
    config: config,
    pkg: grunt.file.readJSON('package.json'),

    // Task configuration goes here.

    concat: {
      app: {
        src: ['<%= config.src %>/static/js/app/**/*.js'],
        dest: '<%= config.build %>/static/js/app.js'
      },
      vendor: {
        src: ['<%= config.src %>/static/js/vendor/**/*.js'],
        dest: '<%= config.build %>/static/js/lib.js'
      }
    },

    uglify: {
      app: {
        files: {
          '<%= config.build %>/static/js/app.min.js': ['<%= config.src %>/static/js/app/**/*.js']
        }
      },
      vendor: {
        files: {
          '<%= config.build %>/static/js/lib.min.js': ['<%= config.src %>/static/js/vendor/**/*.js']
        }
      }
    },

    sass: {
      dev: {
        options: {
          sourceMap: true
        },
        files: {
          '<%= config.build %>/static/css/main.css': '<%= config.src %>/static/scss/main.scss'
        }
      },
      deploy: {
        options: {
          sourceMap: true,
          outputStyle: 'compressed'
        },
        files: {
          '<%= config.build %>/static/css/main.min.css': '<%= config.src %>/static/scss/main.scss'
        }
      }
    },

    bowercopy: {
      options: {
        srcPrefix: 'bower_components'
      },
      scripts: {
        options: {
          destPrefix: '<%= config.build %>/static/js'
        },
        files: {
          'jquery.min.js': 'jquery/dist/jquery.min.js',
          'materialize.min.js': 'Materialize/dist/js/materialize.min.js',
          'quill.min.js': 'quill/dist/quill.min.js'
        }
      },
      css: {
        options: {
          destPrefix: '<%= config.build %>/static/css'
        },
        files: {
          'materialize.min.css': 'Materialize/dist/css/materialize.min.css',
          'materialdesignicons.min.css': 'mdi/css/materialdesignicons.min.css',
          'quill.base.css': 'quill/dist/quill.base.css',
          'quill.snow.css': 'quill/dist/quill.snow.css'
        }
      },
      fonts: {
        options: {
          destPrefix: '<%= config.build %>/static/fonts'
        },
        files: {
          'materialdesignicons-webfont.eot': 'mdi/fonts/materialdesignicons-webfont.eot',
          'materialdesignicons-webfont.svg': 'mdi/fonts/materialdesignicons-webfont.svg',
          'materialdesignicons-webfont.ttf': 'mdi/fonts/materialdesignicons-webfont.ttf',
          'materialdesignicons-webfont.woff': 'mdi/fonts/materialdesignicons-webfont.woff',
          'materialdesignicons-webfont.woff2': 'mdi/fonts/materialdesignicons-webfont.woff2'
        }
      }
    },

    imagemin: { // Task
      dynamic: { // Another target
        files: [{
          expand: true, // Enable dynamic expansion
          cwd: '<%= config.src %>/static/images/', // Src matches are relative to this path
          src: ['**/*.{png,jpg,gif}'], // Actual patterns to match
          dest: '<%= config.build %>/static/images/' // Destination path prefix
        }]
      }
    },

    watch: {
      options: {
        livereload: true
      },
      javascript: {
        files: ['<%= config.src %>/static/js/app/**/*.js'],
        tasks: ['concat']
      },
      sass: {
        files: '<%= config.src %>/static/scss/**/*.scss',
        tasks: ['sass:dev']
      }
    }

  });

  // Load plugins here.
  grunt.loadNpmTasks('grunt-contrib-concat');
  grunt.loadNpmTasks('grunt-contrib-uglify');
  grunt.loadNpmTasks('grunt-sass');
  grunt.loadNpmTasks('grunt-bowercopy');
  grunt.loadNpmTasks('grunt-contrib-less');
  grunt.loadNpmTasks('grunt-contrib-imagemin');
  grunt.loadNpmTasks('grunt-contrib-watch');

  // Register tasks here.
  grunt.registerTask('default', [
    'concat',
    'uglify',
    'sass',
    'bowercopy',
    'imagemin'
  ]);

};
