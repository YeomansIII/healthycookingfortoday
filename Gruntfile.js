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
        dest: 'django-project/build/static/js/app.js'
      },
      vendor: {
        src: ['<%= config.src %>/static/js/vendor/**/*.js'],
        dest: 'django-project/build/static/js/lib.js'
      }
    },

    uglify: {
      app: {
        files: {
          'django-project/build/static/js/app.min.js': ['<%= config.src %>/static/js/app/**/*.js']
        }
      },
      vendor: {
        files: {
          'django-project/build/static/js/lib.min.js': ['<%= config.src %>/static/js/vendor/**/*.js']
        }
      }
    },

    sass: {
      dev: {
        options: {
          sourceMap: true
        },
        files: {
          'django-project/build/static/css/main.css': '<%= config.src %>/static/scss/main.scss'
        }
      },
      deploy: {
        options: {
          sourceMap: true,
          outputStyle: 'compressed'
        },
        files: {
          'django-project/build/static/css/main.min.css': '<%= config.src %>/static/scss/main.scss'
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
          'materialize.min.js': 'Materialize/dist/js/materialize.min.js'
        }
      },
      css: {
        options: {
          destPrefix: '<%= config.build %>/static/css'
        },
        files: {
          'materialize.min.css': 'Materialize/dist/css/materialize.min.css',
          'materialdesignicons.min.css': 'mdi/css/materialdesignicons.min.css',
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
          cwd: 'django-project/static/images/', // Src matches are relative to this path
          src: ['**/*.{png,jpg,gif}'], // Actual patterns to match
          dest: 'django-project/build/static/images/' // Destination path prefix
        }]
      }
    },

    watch: {
      options: {
        livereload: true
      },
      javascript: {
        files: ['django-project/static/js/app/**/*.js'],
        tasks: ['concat']
      },
      sass: {
        files: 'django-project/static/scss/**/*.scss',
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
    'imagemin',
    'watch'
  ]);

};
