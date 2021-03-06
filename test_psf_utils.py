#!/usr/bin/env python3
# encoding: utf8

from psf_utils import PSF
from inform import Error, display
from pytest import raises, approx


def test_ac_lin():
    try:
        psf = PSF('samples/pnoise.raw/aclin.ac')
        sweep = psf.get_sweep()
        assert sweep.name == 'freq', 'sweep'
        assert sweep.units == 'Hz', 'sweep'
        assert len(sweep.abscissa) == 1001, 'sweep'
        assert isinstance(sweep.abscissa[0], float), 'sweep'

        signals = {
            'iRESref:p': ('A', 'complex double'),
            'iRESva:p':  ('A', 'complex double'),
            'noiref':    ('V', 'complex double'),
            'noiva':     ('V', 'complex double'),
            'top':       ('V', 'complex double'),
            'topref':    ('V', 'complex double'),
            'topva':     ('V', 'complex double'),
            'VTOP:p':    ('A', 'complex double'),
        }
        for signal in psf.all_signals():
            name = signal.name
            assert name in signals, signal.name
            units, kind = signals.pop(name)
            assert units == signal.units, signal.name
            assert kind == signal.type.kind, signal.name
            if name == 'top':
                assert isinstance(signal.ordinate[0], complex), signal.name
                assert len(signal.ordinate) == 1001
                assert max(signal.ordinate) == 1
                assert min(signal.ordinate) == 1
        assert not signals
    except Error as e:
        e.terminate()


def test_ac_log():
    try:
        psf = PSF('samples/pnoise.raw/aclog.ac')
        sweep = psf.get_sweep()
        assert sweep.name == 'freq', 'sweep'
        assert sweep.units == 'Hz', 'sweep'
        assert len(sweep.abscissa) == 61, 'sweep'
        assert isinstance(sweep.abscissa[0], float), 'sweep'

        signals = {
            'iRESref:p': ('A', 'complex double'),
            'iRESva:p':  ('A', 'complex double'),
            'noiref':    ('V', 'complex double'),
            'noiva':     ('V', 'complex double'),
            'top':       ('V', 'complex double'),
            'topref':    ('V', 'complex double'),
            'topva':     ('V', 'complex double'),
            'VTOP:p':    ('A', 'complex double'),
        }
        for signal in psf.all_signals():
            name = signal.name
            assert name in signals, signal.name
            units, kind = signals.pop(name)
            assert units == signal.units, signal.name
            assert kind == signal.type.kind, signal.name
            if name == 'top':
                assert isinstance(signal.ordinate[0], complex), signal.name
                assert len(signal.ordinate) == 61
                assert max(signal.ordinate) == 1
                assert min(signal.ordinate) == 1
        assert not signals
    except Error as e:
        e.terminate()


def test_noise():
    psf = PSF('samples/pnoise.raw/noiref.noise')
    sweep = psf.get_sweep()
    assert sweep.name == 'freq', 'sweep'
    assert sweep.units == 'Hz', 'sweep'
    assert len(sweep.abscissa) == 121, 'sweep'
    assert isinstance(sweep.abscissa[0], float), 'sweep'

    signals = {
        'RESref:fn':      ('V^2/Hz', 'float double'),
        'RESref:rn':      ('V^2/Hz', 'float double'),
        'RESref:total':   ('V^2/Hz', 'float double'),
        'RESva:flicker':  ('V^2/Hz', 'float double'),
        'RESva:thermal':  ('V^2/Hz', 'float double'),
        'RESva:total':    ('V^2/Hz', 'float double'),
        'Rref:rn':        ('V^2/Hz', 'float double'),
        'Rref:total':     ('V^2/Hz', 'float double'),
        'Rva:rn':         ('V^2/Hz', 'float double'),
        'Rva:total':      ('V^2/Hz', 'float double'),
        'out':            ('V/sqrt(Hz)', 'float double'),
    }
    for signal in psf.all_signals():
        name = signal.name
        assert name in signals, signal.name
        units, kind = signals.pop(name)
        assert units == signal.units, signal.name
        assert kind == signal.type.kind, signal.name
        if name == 'out':
            assert isinstance(signal.ordinate[0], float), signal.name
            assert len(signal.ordinate) == 121
            assert max(signal.ordinate) <= 6e-06
            assert min(signal.ordinate) >= 3e-10
    assert not signals


def test_pnoise():
    psf = PSF('samples/pnoise.raw/pnoiref.pnoise')
    sweep = psf.get_sweep()
    assert sweep.name == 'freq', 'sweep'
    assert sweep.units == 'Hz', 'sweep'
    assert len(sweep.abscissa) == 121, 'sweep'
    assert isinstance(sweep.abscissa[0], float), 'sweep'

    signals = {
        'RESref:fn':      ('V^2/Hz', 'float double'),
        'RESref:rn':      ('V^2/Hz', 'float double'),
        'RESref:total':   ('V^2/Hz', 'float double'),
        'RESva:flicker':  ('V^2/Hz', 'float double'),
        'RESva:thermal':  ('V^2/Hz', 'float double'),
        'RESva:total':    ('V^2/Hz', 'float double'),
        'Rref:rn':        ('V^2/Hz', 'float double'),
        'Rref:total':     ('V^2/Hz', 'float double'),
        'Rva:rn':         ('V^2/Hz', 'float double'),
        'Rva:total':      ('V^2/Hz', 'float double'),
        'out':            ('V/sqrt(Hz)', 'float double'),
    }
    for signal in psf.all_signals():
        name = signal.name
        assert name in signals, signal.name
        units, kind = signals.pop(name)
        assert units == signal.units, signal.name
        assert kind == signal.type.kind, signal.name
        if name == 'out':
            assert isinstance(signal.ordinate[0], float), signal.name
            assert len(signal.ordinate) == 121
            assert max(signal.ordinate) <= 10e-09
            assert min(signal.ordinate) >= 3e-10
    assert not signals


def test_pss_td():
    psf = PSF('samples/pnoise.raw/pss.td.pss')
    sweep = psf.get_sweep()
    assert sweep.name == 'time', 'sweep'
    assert sweep.units == 's', 'sweep'
    assert len(sweep.abscissa) == 1601, 'sweep'
    assert isinstance(sweep.abscissa[0], float), 'sweep'

    signals = {
        'VTOP:p':    ('A', 'float double'),
        'iRESref:p': ('A', 'float double'),
        'iRESva:p':  ('A', 'float double'),
        'noiref':    ('V', 'float double'),
        'noiva':     ('V', 'float double'),
        'top':       ('V', 'float double'),
        'topref':    ('V', 'float double'),
        'topva':     ('V', 'float double'),
    }
    for signal in psf.all_signals():
        name = signal.name
        assert name in signals, signal.name
        units, kind = signals.pop(name)
        assert units == signal.units, signal.name
        assert kind == signal.type.kind, signal.name
        if name == 'top':
            assert isinstance(signal.ordinate[0], float), signal.name
            assert len(signal.ordinate) == 1601
            assert max(signal.ordinate) <= 0.1
            assert min(signal.ordinate) >= -0.1
    assert not signals


if __name__ == '__main__':
    # As a debugging aid allow the tests to be run on their own, outside pytest.
    # This makes it easier to see and interpret and textual output.
    from inform import Error

    defined = dict(globals())
    for k, v in defined.items():
        try:
            if callable(v) and k.startswith('test_'):
                print()
                print('Calling:', k)
                print((len(k)+9)*'=')
                v()
        except Error as e:
            e.report()
