<script lang="ts">
    export let text: string;
    export let side: 'left' | 'right' = 'left';
    export let color: string = 'var(--accent)';
</script>

<span class={`bookmark bookmark-${side}`} style={`--label-color: ${color};`}>
    {text}
</span>

<style>
    .bookmark {
        position: absolute;
        top: 0.55rem;
        display: inline-block;
        padding: 0.25rem 0.75rem;
        font-size: 0.78rem;
        font-weight: 700;
        letter-spacing: 0.04em;
        text-transform: uppercase;
        color: var(--bg);
        background: var(--label-color);
        border-radius: 0.4rem 0.4rem 0.15rem 0.15rem;
        box-shadow: 0 4px 10px color-mix(in srgb, var(--label-color) 35%, transparent);
    }

    .bookmark::after {
        content: "";
        position: absolute;
        left: 50%;
        transform: translateX(-50%);
        bottom: -0.35rem;
        width: 0;
        height: 0;
        border-left: 0.34rem solid transparent;
        border-right: 0.34rem solid transparent;
        border-top: 0.36rem solid color-mix(in srgb, var(--label-color) 70%, black);
    }

    .bookmark-left {
        left: 0.75rem;
    }

    .bookmark-right {
        right: 0.75rem;
    }

</style>
