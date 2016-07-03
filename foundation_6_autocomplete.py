import sublime_plugin
import sublime

# The following 2 lines can be generated with "grunt sublime" in the main foundation code
foundation_classes = ["map_canvas","is-visible","is-hidden","row","collapse","expanded","column","columns","end","small-1","small-push-1","small-pull-1","small-offset-0","small-2","small-push-2","small-pull-2","small-offset-1","small-3","small-push-3","small-pull-3","small-offset-2","small-4","small-push-4","small-pull-4","small-offset-3","small-5","small-push-5","small-pull-5","small-offset-4","small-6","small-push-6","small-pull-6","small-offset-5","small-7","small-push-7","small-pull-7","small-offset-6","small-8","small-push-8","small-pull-8","small-offset-7","small-9","small-push-9","small-pull-9","small-offset-8","small-10","small-push-10","small-pull-10","small-offset-9","small-11","small-push-11","small-pull-11","small-offset-10","small-12","small-offset-11","small-up-1","small-up-2","small-up-3","small-up-4","small-up-5","small-up-6","small-up-7","small-up-8","small-collapse","small-uncollapse","small-centered","small-pull-0","small-push-0","small-uncentered","medium-push-1","medium-pull-1","medium-offset-0","medium-2","medium-push-2","medium-pull-2","medium-offset-1","medium-3","medium-push-3","medium-pull-3","medium-offset-2","medium-4","medium-push-4","medium-pull-4","medium-offset-3","medium-5","medium-push-5","medium-pull-5","medium-offset-4","medium-6","medium-push-6","medium-pull-6","medium-offset-5","medium-7","medium-push-7","medium-pull-7","medium-offset-6","medium-8","medium-push-8","medium-pull-8","medium-offset-7","medium-9","medium-push-9","medium-pull-9","medium-offset-8","medium-10","medium-push-10","medium-pull-10","medium-offset-9","medium-11","medium-push-11","medium-pull-11","medium-offset-10","medium-12","medium-offset-11","medium-up-1","medium-up-2","medium-up-3","medium-up-4","medium-up-5","medium-up-6","medium-up-7","medium-up-8","medium-collapse","medium-uncollapse","medium-centered","medium-pull-0","medium-push-0","medium-uncentered","large-push-1","large-pull-1","large-offset-0","large-2","large-push-2","large-pull-2","large-offset-1","large-3","large-push-3","large-pull-3","large-offset-2","large-4","large-push-4","large-pull-4","large-offset-3","large-5","large-push-5","large-pull-5","large-offset-4","large-6","large-push-6","large-pull-6","large-offset-5","large-7","large-push-7","large-pull-7","large-offset-6","large-8","large-push-8","large-pull-8","large-offset-7","large-9","large-push-9","large-pull-9","large-offset-8","large-10","large-push-10","large-pull-10","large-offset-9","large-11","large-push-11","large-pull-11","large-offset-10","large-12","large-offset-11","large-up-1","large-up-2","large-up-4","large-up-5","large-up-6","large-up-7","large-up-8","large-collapse","large-uncollapse","large-centered","large-pull-0","large-push-0","large-uncentered","subheader","lead","stat","no-bullet","text-left","text-right","text-center","text-justify","medium-text-right","medium-text-center","medium-text-justify","large-text-right","large-text-center","large-text-justify","show-for-print","hide-for-print","button","tiny","small","large","primary","secondary","success","warning","alert","hollow","disabled","dropdown","arrow-only","middle","help-text","input-group","input-group-label","input-group-field","input-group-button","fieldset","is-invalid-input","form-error","is-invalid-label","form-erro","accordion","accordion-item","accordion-title","accordion-content","is-accordion-submenu-parent","badge","breadcrumbs","button-group","stacked-for-medium","stacked-for-smal","stacked","callout","close-button","menu","vertical","medium-vertical","large-vertical","simple","align-right","icon-top","nested","active","menu-text","menu-centered","no-js","menu-icon","is-drilldown","is-drilldown-submenu","is-active","is-closing","dropdown-pane","is-open","opens-left","is-dropdown-submenu","opens-right","is-dropdown-submenu-parent","medium-horizontal","large-horizontal","first-sub","is-dropdown-menu","opens-inner","js-dropdown-active","flex-video","widescreen","vimeo","label","media-object","media-object-section","bottom","off-canvas-wrapper","off-canvas-wrapper-inner","off-canvas-content","js-off-canvas-exit","off-canvas","position-left","is-open-left","position-right","is-open-right","orbit","orbit-container","orbit-slide","no-motionui","orbit-figure","orbit-image","orbit-caption","orbit-next","orbit-previous","orbit-bullets","pagination","current","ellipsis","pagination-previous","pagination-next","progress","progress-meter","progress-meter-text","is-reveal-open","reveal-overlay","reveal","full","without-overlay","slider","slider-fill","is-dragging","slider-handle","sticky-container","sticky","is-stuck","is-at-top","is-at-bottom","is-anchored","switch","switch-input","switch-paddle","switch-active","switch-inactive","stack","table-scroll","tabs","tabs-title","tabs-content","tabs-panel","thumbnail","title-bar","title-bar-left","title-bar-right","title-bar-title","dark","has-tip","tooltip","top","left","right","top-bar","top-bar-left","top-bar-right","top-bar-title","hide","invisible","show-for-sr","show-on-focus","hide-for-portrait","show-for-landscape","hide-for-landscape","show-for-portrait","float-left","float-right","float-center","clearfix","slide-in-down","mui-enter","mui-enter-active","slide-in-left","slide-in-up","slide-in-right","slide-out-down","mui-leave","mui-leave-active","slide-out-right","slide-out-up","slide-out-left","fade-in","fade-out","hinge-in-from-top","hinge-in-from-right","hinge-in-from-bottom","hinge-in-from-left","hinge-in-from-middle-x","hinge-in-from-middle-y","hinge-out-from-top","hinge-out-from-right","hinge-out-from-bottom","hinge-out-from-left","hinge-out-from-middle-x","hinge-out-from-middle-y","scale-in-up","scale-in-down","scale-out-up","scale-out-down","spin-in","spin-out","spin-in-ccw","spin-out-ccw","slow","fast","linear","ease","ease-in","ease-out","ease-in-out","bounce-in","bounce-out","bounce-in-out","short-delay","long-delay","shake","spin-cw","spin-ccw","wiggle","infinite",]

class FoundationCompletions(sublime_plugin.EventListener):
    """
    Provide tag completions for Foundation elements and data-uk attributes
    """
    def __init__(self):

        self.class_completions = [("%s \tFoundation 3 Class" % s, s) for s in foundation_classes]

    def on_query_completions(self, view, prefix, locations):

        if view.match_selector(locations[0], "text.html string.quoted"):

            # Cursor is inside a quoted attribute
            # Now check if we are inside the class attribute

            # max search size
            LIMIT  = 250

            # place search cursor one word back
            cursor = locations[0] - len(prefix) - 1

            # dont start with negative value
            start  = max(0, cursor - LIMIT - len(prefix))

            # get part of buffer
            line   = view.substr(sublime.Region(start, cursor))

            # split attributes
            parts  = line.split('=')

            # is the last typed attribute a class attribute?
            if len(parts) > 1 and parts[-2].strip().endswith("class"):
                return self.class_completions
            else:
                return []
        elif view.match_selector(locations[0], "text.html meta.tag - text.html punctuation.definition.tag.begin"):

            # Cursor is in a tag, but not inside an attribute, i.e. <div {here}>
            # This one is easy, just return completions for the data-uk-* attributes
            return self.data_completions

        else:

            return []
