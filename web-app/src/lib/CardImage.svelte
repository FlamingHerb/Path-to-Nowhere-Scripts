<div class="matcard">
    <slot />
</div>

<style lang="scss">
    @font-face {
        font-family: 'DFLiSong Std W7';
        font-style: normal;
        font-weight: 400;
        src: url('/fonts/DFLiSongStd-W7.otf') format('opentype');
    }

    @font-face {
        font-family: 'SUIT SemiBold';
        font-style: normal;
        font-weight: 400;
        src: url('/fonts/SUIT-SemiBold.ttf') format('truetype');
    }

    @font-face {
        font-family: 'HYQiHeiB5-55';
        font-style: normal;
        font-weight: 400;
        src: url('/fonts/HYQiHeiB5-55.ttf') format('truetype');
    }

    .matcard {
        background-color: #000;
        position: relative;
        border: 1px solid #6B7998;
        max-height: 96px;
        max-width: 96px;
    }
    .matcard :global(> :last-child) {
        font-family: 'HYQiHeiB5-55';
        position:absolute;
        background-color: rgba(0,0,0,0.5);
        color: #fff;
        text-align: right;
        width: 91px;
        padding-right: 5px;
        bottom:0;
        right:0;
    }
</style>

