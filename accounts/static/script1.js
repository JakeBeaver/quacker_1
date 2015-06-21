// Backbone Model

app.__definitions.models.Signup = Backbone.Model.extend({
    url: '/app/signup',

    defaults: {
            name: '',
            email: '',
            password: ''
    },

    validateOne: validator.validateOne,

    validate: function(fields) {
            var result = validator.validateAll(fields);
            if (result !== true) return result;
    }
 });

// Backbone Views

app.__definitions.views.Signup = Backbone.View.extend({
    el: $('form'),

    events: {
        'submit': 'onFormSubmit',
        'change input[type!="submit"]': 'onInputChange',
        'blur input[type!="submit"]': 'onInputChange',
        'focus input': function(e) {
                this.resetInputErrors(e.target);
        }
    },

    templates: {
            'error': _.template('<span class="error"><%=error%></span>')
    },

    initialize: function() {
            this.model = new app.__definitions.models.Signup();

            this.model.on('invalid', this.onModelInvalid, this);
    },

    getInput: function(name) {
            return this.$el.find('[name="' + name + '"]');
    },

    onModelInvalid: function(model, errors) {
            var _this = this;
            _.each(errors, function(error, name) {
                    _this.showInputErrors(_this.getInput(name), error);
            }) 
    },

    onFormSubmit: function(e) {
            e.preventDefault();
            var model = this.model;

            this.$el.find('input[name]').each(function() {
                    model.set(this.name, this.value);
            })
            this.model.save();
    },

    onInputChange: function(e) {
            this.model.set(e.target.name, e.target.value);
            var result = this.model.validateOne(e.target.name, e.target.value);
            if (result !== true) this.showInputErrors(e.target, result)
    },

    resetInputErrors: function(target) {
            var $target = $(target);
            $target.removeClass('incorrect')
            $target.parent().find('.error').remove();
    },

    showInputErrors: function(target, errors) {
            var $target = $(target);
            var errorsHTML = '';

            this.resetInputErrors(target);

            for (var i = 0; i < errors.length; i++) {
                    errorsHTML += this.templates.error({error: se.errors.get(errors[i])});
            }

            $target.addClass('incorrect'); 
            $target.parent().append(errorsHTML);
    }
    });